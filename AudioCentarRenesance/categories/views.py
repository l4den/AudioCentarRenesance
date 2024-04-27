from django.shortcuts import render


def all_categories_page(request):
    return render(request, 'categories/categories_page.html')
