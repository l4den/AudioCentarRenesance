# Generated by Django 5.0.4 on 2024-04-30 11:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0014_delete_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='parent',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='categories.maincategory'),
        ),
    ]