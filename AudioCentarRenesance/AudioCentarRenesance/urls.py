"""
URL configuration for AudioCentarRenesance project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('rosetta/', include('rosetta.urls')),
    path('', views.home_page, name='home_page'),
    path('search/', views.search, name='search'),
    path('about-us', views.about_us_page, name='about_us_page'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('store/', include('products.urls')),
    path('contact/', include('contacts.urls')),
    path('categories/', include('categories.urls')),
    path('switch_language/<str:code>', views.switch_language, name='switch_language'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
