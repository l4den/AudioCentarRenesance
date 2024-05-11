from .models import MainCategory, SubCategory


def menu_links(request):
    categories = MainCategory.objects.all()
    subcategories = SubCategory.objects.all()
    store_paths = ['/mk/store/', '/en/store/', '/sq/store/']
    return dict(categories=categories, subcategories=subcategories, store_paths=store_paths)