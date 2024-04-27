from django.contrib import admin
from .models import Product, ProductGallery
import admin_thumbnails
import math


@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1
    max_num = 10
    fk_name = 'product'


@admin_thumbnails.thumbnail('main_image')
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'discount', 'total_price', 'stock', 'category', 'get_modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}
    inlines = [ProductGalleryInline]

    class Media:
        js = ('product_admin.js',)

    def get_modified_date(self, obj):
        return obj.modified_date.strftime('%d %B, %Y, %H:%M')
    get_modified_date.short_description = 'Modified Date'

    def save_model(self, request, obj, form, change):
        # calculate total_price = price - discount + tax
        obj.total_price = math.ceil((obj.price * (1 - obj.discount/100) ) * obj.tax)
        obj.price_wo_discount = math.ceil(obj.price * obj.tax)
        
        super().save_model(request, obj, form, change)


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductGallery)