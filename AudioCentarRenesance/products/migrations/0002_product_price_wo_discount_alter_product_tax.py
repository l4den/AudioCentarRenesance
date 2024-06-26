# Generated by Django 5.0.4 on 2024-04-08 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price_wo_discount',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='tax',
            field=models.FloatField(choices=[(1.18, 'A: 18%'), (1.05, 'Б: 5%'), (1.1, 'В: 10%'), (1.0, 'Г: 0%')], default=1.0),
        ),
    ]
