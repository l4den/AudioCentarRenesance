from django.urls import path
from . import views

urlpatterns = [
    path('all', views.all_categories_page, name='all_categories_page'),
]