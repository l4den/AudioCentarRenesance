from django.db import models
from django.utils.translation import gettext_lazy as _

class MainCategory(models.Model):
    category_name = models.CharField(_('Name'), max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(_('Description'), max_length=255, blank=True)
    image = models.ImageField(_('Image'), default='default_category_image.jpg', upload_to='category_photos')

    class Meta:
        verbose_name = _('MainCategory')
        verbose_name_plural = _('MainCategories')

    def get_url(self):
        return reverse('product_by_cat', args=[self.slug])

    def __str__(self):
        return self.category_name


class SubCategory(models.Model):
    category_name = models.CharField(_('Name'), max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(_('Description'), max_length=255, blank=True)
    parent = models.ForeignKey(MainCategory, on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name = _('SubCategory')
        verbose_name_plural = _('SubCategories')

    def get_url(self):
        return reverse('product_by_cat', args=[self.slug])

    def __str__(self):
        return self.category_name