from django.contrib import admin
from .models import Brand
import admin_thumbnails


@admin_thumbnails.thumbnail('image')
class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand_name', 'slug')
    prepopulated_fields = {'slug': ('brand_name',)}


admin.site.register(Brand, BrandAdmin)