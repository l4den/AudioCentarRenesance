# Generated by Django 5.0.4 on 2024-04-22 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0002_alter_brand_brand_name_alter_brand_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brand_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='brand',
            name='description',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='brand',
            name='image',
            field=models.ImageField(default='category_default_img.jpg', upload_to='brand_photos'),
        ),
    ]
