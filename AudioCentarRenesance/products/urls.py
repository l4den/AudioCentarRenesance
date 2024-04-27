from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.store_page, name='store_page'),
    path('filter', views.filter_data, name='filter_data'),
    path('category/<slug:category_slug>/product/<slug:product_slug>', views.product_details, name='product_details_page'),
]
