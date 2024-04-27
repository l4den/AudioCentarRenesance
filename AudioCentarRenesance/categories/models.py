from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    category_name = models.CharField(_('Name'), max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(_('Description'), max_length=255, blank=True)
    image = models.ImageField(_('Image'), default='default_category_image.jpg', upload_to='category_photos')


    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def get_url(self):
        return reverse('product_by_cat', args=[self.slug])

    def __str__(self):
        return self.category_name