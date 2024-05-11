from django.shortcuts import render, redirect
from django.http import JsonResponse
from categories.models import MainCategory, SubCategory
from django.db.models import Count, Min, Max
from brands.models import Brand
from products.models import Product, ProductGallery
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils import timezone


def store_page(request):
    # pre selected
    selected_category = request.GET.get('category')
    on_discount = request.GET.get('on_discount')
    is_new = request.GET.get('is_new')
    selected_sub_category = request.GET.get('sub_category')

    # filter variables
    main_categories = MainCategory.objects.annotate(product_count=Count('subcategory__product'))
    sub_categories = SubCategory.objects.annotate(product_count=Count('product'))
    brands = Brand.objects.annotate(product_count=Count('product'))
    min_total_price = Product.objects.aggregate(min_total_price=Min('total_price'))
    max_total_price = Product.objects.aggregate(max_total_price=Max('total_price'))
    discount_count = Product.objects.filter(discount__gt=0).count()
    new_count = Product.objects.filter(created_date__gt=(timezone.now() - timezone.timedelta(days=7))).count()

    if selected_category:
        sub_cats = SubCategory.objects.filter(parent__slug=selected_category)
        selected_sub_category = [sub_cat.slug for sub_cat in sub_cats]
        products = Product.objects.filter(category__in=sub_cats).order_by('-created_date')
    elif selected_sub_category:
        products = Product.objects.filter(category__slug=selected_sub_category).order_by('-created_date')
        selected_sub_category = [selected_sub_category]
    else:
        products = Product.objects.all().order_by('-created_date')

    if on_discount:
        products = products.filter(discount__gt=0)

    if is_new:
        products = products.filter(created_date__gt=(timezone.now() - timezone.timedelta(days=7)))
    
    context = {'main_categories': main_categories,
               'sub_categories': sub_categories, 
               'brands': brands,
               'products': products,
               'min_price': min_total_price['min_total_price'],
               'max_price': max_total_price['max_total_price'],
               'selected_category': selected_category,
               'selected_sub_category': selected_sub_category,
               'discount_count': discount_count,
               'on_discount': on_discount,
               'new_count': new_count,
               'is_new': is_new,}

    return render(request, 'products/store.html', context)


def filter_data(request):
    categories = request.GET.getlist('category[]')
    brands = request.GET.getlist('brand[]')
    sorting = request.GET.get('sort')
    discount = request.GET.get('discount[]')
    new = request.GET.get('new[]')
    min_price = int(request.GET.get('min_price'))
    max_price = int(request.GET.get('max_price'))
    sub_categories = request.GET.getlist('sub_category[]')
    products = Product.objects.all()


    products = products.filter(total_price__gte=min_price, total_price__lte=max_price)

    sub_categories_ids = [int(id) for id in sub_categories]

    if len(categories) > 0 and len(sub_categories_ids) > 0:
        subcategories = list(SubCategory.objects.filter(parent__in = categories).values_list('id', flat=True))

        all_sub_categories = set(sub_categories_ids).union(set(subcategories))
        all_sub_categories = list(all_sub_categories)

        products = products.filter(category__in=list(all_sub_categories)).distinct()
        
    elif len(categories) > 0:
        subcategories = list(SubCategory.objects.filter(parent__in = categories).values_list('id', flat=True))
        products = products.filter(category__in=subcategories).distinct()

    elif len(sub_categories_ids) > 0:
        products = products.filter(category__in=sub_categories_ids).distinct()

    if len(brands) > 0:
         products = products.filter(brand_id__in=brands).distinct()

    if discount != None:
        products = products.filter(discount__gt=0).distinct()

    if new != None:
        products = products.filter(created_date__gt=(timezone.now() - timezone.timedelta(days=7))).distinct()
    
    if sorting == 'low':
        products = products.order_by('total_price')
    elif sorting == 'high':
        products = products.order_by('-total_price')
    else:
        products = products.order_by('-created_date')

    t = render_to_string('ajax/product-list.html', {'data': products})
    return JsonResponse({'data': t})


def product_details(request, category_slug, product_slug):
    try:
        product = Product.objects.get(slug=product_slug)
    except ObjectDoesNotExist:
        messages.error(request, 'Product does not exist')
        return redirect('store_page')

    product_gallery = ProductGallery.objects.filter(product=product)

    lower_bound = product.total_price*0.8
    higher_bound = product.total_price*1.2

    related_products = Product.objects.filter(category=product.category,
                                              total_price__gte=lower_bound,
                                              total_price__lte=higher_bound).exclude(id=product.id).order_by('created_date')[:4]

    context = {'product': product, 
               'product_gallery': product_gallery, 
               'related_products': related_products}
    return render(request, 'products/product.html', context)