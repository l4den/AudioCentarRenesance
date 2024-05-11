from django.db import models
from django.utils import timezone
from categories.models import SubCategory
from brands.models import Brand
from django.urls import reverse
import math
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    product_name = models.CharField(_('Name'), max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(_('Description'), max_length=500, blank=True)
    product_info = models.TextField(_('Information'), max_length=500, blank=True)

    price = models.PositiveIntegerField(_('Price'))
    discount = models.PositiveIntegerField(_('Discount'), default=0)

    VAT_OPTIONS = [
                (1.18, 'A: 18%'),
                (1.05, 'Б: 5%'),
                (1.1, 'В: 10%'),
                (1.0, 'Г: 0%'),
            ]
    tax = models.FloatField(_('Tax'), choices=VAT_OPTIONS, default=1.0)
    total_price = models.PositiveIntegerField(_('Total_price'), blank=True)

    stock = models.PositiveIntegerField(_('Stock'), )
    is_available = models.BooleanField(_('Available'), default=True)
    top_selling = models.BooleanField(_('Top_selling'), default=False)

    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)    # if cateogry is deleted all products in that category will be deleted
    brand = models.ForeignKey(Brand , on_delete=models.CASCADE)

    main_image = models.ImageField(_('Image'), default='default_product_img.jpg', upload_to='products')

    created_date = models.DateTimeField(_('Date_created'), auto_now_add=True)
    modified_date = models.DateTimeField(_('Date_modified'), auto_now=True)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def get_url(self):
        return reverse('product_details_page', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name

    def is_new(self):
        seven_days_ago = timezone.now() - timezone.timedelta(days=7)
        
        return self.created_date > seven_days_ago

    def price_no_discount(self):
        return math.ceil(self.price * self.tax)


class ProductGallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(_('Image'), upload_to='products', max_length=255)

    def __str__(self):
        return self.product.product_name + ' image'

    class Meta:
        verbose_name = _('ProductGallery')
        verbose_name_plural = _('ProductGalleries')
