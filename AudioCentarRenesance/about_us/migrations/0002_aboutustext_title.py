# Generated by Django 5.0.4 on 2024-05-20 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutustext',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]