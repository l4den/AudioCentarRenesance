# Generated by Django 5.0.4 on 2024-04-09 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(default='default_category_image.jpg', upload_to='category_photos'),
        ),
    ]
