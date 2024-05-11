from django.shortcuts import render, redirect
from products.models import Product
from django.utils import timezone
from categories.models import MainCategory, SubCategory
from contacts.models import NewsLetter
from django.contrib import messages
from django.db.models import Count
from about_us.models import AboutUsText, AboutUsImage
from brands.models import Brand
from django.core.exceptions import ObjectDoesNotExist
import math
import random

def generate_new_products(start, end):

    categories = SubCategory.objects.all()
    brands = Brand.objects.all()

    for index in range(start, end):
        category = categories[random.randint(0,11)]
        if random.choice([True, False]):
            discount = random.randint(0,30)
        else:
            discount = 0
        price = index * random.randint(100, 1000)
        
        Product.objects.create(product_name=f'Testing Product {index}',
                                slug=f'testing-product-{index}',
                                description=f'Testing Product {index} description',
                                product_info=f'Testing Product {index} information',
                                price=price ,
                                discount=discount,
                                tax=1.18,
                                total_price=(price*(1-(discount/100)))*1.18,
                                stock=10*index,
                                is_available=True,
                                top_selling=random.choice([True, False]),
                                category=category,
                                brand=brands[random.randint(0,5)],)

            


def home_page(request):
    #generate_new_products(12, 30)

    products = Product.objects.all()
    new_products = products.filter(created_date__gt=(timezone.now() - timezone.timedelta(days=7)))[:10]

    main_categories = MainCategory.objects.all()

    top_selling_products = products.filter(top_selling=True)[:6]

    brands = Brand.objects.all()

    context = {
        'products': products,
        'new_products': new_products,
        'main_categories': main_categories,
        'brands': brands,
        'top_selling_products': top_selling_products, 
    }

    return render(request, 'index.html', context)


def search(request):
    keyword = request.GET.get('keyword')
    category_slug = request.GET.get('category')
    main_category = 'all'

    if category_slug == 'all':
        products = Product.objects.filter(product_name__icontains=keyword)
    else:
        try:
            main_category = MainCategory.objects.get(slug=category_slug).category_name
        except ObjectDoesNotExist:
            messages.error(request, 'No such category found')
            return redirect('home_page')

        sub_categories = SubCategory.objects.filter(parent__slug=category_slug)
        products = Product.objects.filter(category__in=sub_categories, product_name__icontains=keyword)  

    
    context = {'products': products,
               'keyword': keyword,
               'category': main_category}

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
    images = AboutUsImage.objects.all()
    text = AboutUsText.objects.last()
    context = {
        'images': images,
        'text': text
    }
    return render(request, 'about_us.html', context)


def switch_language(request, code):
    if code in ['en', 'mk', 'sq']:
        previous_url = request.META.get('HTTP_REFERER')[24:]
        return redirect('/' + code + previous_url)

    else:
        messages.error(request, f'Language code {code} is not supported.')
        return redirect('home_page')