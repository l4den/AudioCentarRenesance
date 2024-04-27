from django.db import models
from django.utils.translation import gettext_lazy as _


class Brand(models.Model):
    brand_name = models.CharField(_('Name'), max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.CharField(_('Description'), max_length=500, blank=True)
    image = models.ImageField(_('Image'), default='category_default_img.jpg', upload_to='brand_photos')

    class Meta:
        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')

    def __str__(self):
        return self.brand_name