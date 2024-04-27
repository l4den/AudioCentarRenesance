from django.shortcuts import render, redirect
from products.models import Product
from django.utils import timezone
from categories.models import Category
from contacts.models import NewsLetter
from django.contrib import messages
from django.db.models import Count
import math
# from brands.models import Brand

    # category = Category.objects.first()
    # brand = Brand.objects.first()

    # for prod in range(1,11):
    #     Product.objects.create(product_name=f'Testing Product {prod}',
    #                            slug=f'testing-product-{prod}',
    #                            description=f'Testing Product {prod} description',
    #                            product_info=f'Testing Product {prod} information',
    #                            price=1000*prod,
    #                            discount=0,
    #                            tax=1.18,
    #                            total_price=(1000*prod)*1.18,
    #                            stock=10*prod,
    #                            is_available=True,
    #                            top_selling=True,
    #                            category=category,
    #                            brand=brand,)

    # for i, prod in enumerate(top_selling_products):
    #     if i % 2:
    #         prod.discount = i*2
    #         actual_discount = 1 - (i*2)/100
    #         prod.total_price = math.ceil( (prod.price * actual_discount) * prod.tax)
    #         print(f'{prod.total_price} = {prod.price} * {actual_discount} * {prod.tax}')
    #         prod.save()


def home_page(request):
    products = Product.objects.all()
    new_products = products.filter(created_date__gt=(timezone.now() - timezone.timedelta(days=7)))[:10]

    top_3_categories = Category.objects.annotate(product_count=Count('product')).order_by('-product_count')[:3]

    top_selling_products = products.filter(top_selling=True)[:6]


    context = {
        'products': products,
        'new_products': new_products,
        'top_3_categories': top_3_categories,
        'top_selling_products': top_selling_products, 
    }

    return render(request, 'index.html', context)


def search(request):
    keyword = request.GET.get('keyword')
    category_name = request.GET.get('category')

    if category_name != 'all': 
        products = Product.objects.filter(category__category_name=category_name, product_name__icontains=keyword)
    else:  
        products = Product.objects.filter(product_name__icontains=keyword)

    
    context = {'products': products,
               'keyword': keyword,
               'category': category_name}

    return render(request, 'search_result.html', context)


def newsletter(request):
    if request.method == 'GET':
        email = request.GET.get('newsletter')
        
        if email and '@' in email and '.' in email and email.index('@') < email.rindex('.'):
            if NewsLetter.objects.filter(email=email).exists():
                messages.info(request, 'You are already subscribed to our newsletter.')
            else:
                newsletter = NewsLetter.objects.create(email=email)
                newsletter.save()
                messages.success(request, 'You have successfully subscribed to our newsletter.')
        else:
            messages.error(request, 'Invalid email format. Please enter a valid email address.')
            
    return redirect('home_page')



def about_us_page(request):
    return render(request, 'about_us.html')


def switch_language(request, code):
    if code in ['en', 'mk', 'sq']:
        previous_url = request.META.get('HTTP_REFERER')[24:]
        return redirect('/' + code + previous_url)

    else:
        messages.error(request, f'Language code {code} is not supported.')
        return redirect('home_page')