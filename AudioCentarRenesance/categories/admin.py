from django.contrib import admin
from .models import MainCategory, SubCategory
import admin_thumbnails


@admin_thumbnails.thumbnail('image')
class MainCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name', )}
    list_display = ('category_name', 'slug',)

class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name', )}
    list_display = ('category_name', 'slug', 'parent')


admin.site.register(MainCategory, MainCategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)

