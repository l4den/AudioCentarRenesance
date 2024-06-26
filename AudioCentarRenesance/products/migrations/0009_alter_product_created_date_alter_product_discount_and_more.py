# Generated by Django 5.0.4 on 2024-04-22 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date_created'),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.PositiveIntegerField(default=0, verbose_name='Discount'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_available',
            field=models.BooleanField(default=True, verbose_name='Available'),
        ),
        migrations.AlterField(
            model_name='product',
            name='main_image',
            field=models.ImageField(default='default_product_img.jpg', upload_to='products', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Date_modified'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_info',
            field=models.TextField(blank=True, max_length=500, verbose_name='Information'),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.PositiveIntegerField(verbose_name='Stock'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tax',
            field=models.FloatField(choices=[(1.18, 'A: 18%'), (1.05, 'Б: 5%'), (1.1, 'В: 10%'), (1.0, 'Г: 0%')], default=1.0, verbose_name='Tax'),
        ),
        migrations.AlterField(
            model_name='product',
            name='top_selling',
            field=models.BooleanField(default=False, verbose_name='Top_selling'),
        ),
        migrations.AlterField(
            model_name='product',
            name='total_price',
            field=models.PositiveIntegerField(blank=True, verbose_name='Total_price'),
        ),
    ]
