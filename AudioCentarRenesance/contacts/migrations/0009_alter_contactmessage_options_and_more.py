# Generated by Django 5.0.4 on 2024-04-22 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0008_alter_contactmessage_date_sent_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactmessage',
            options={'verbose_name': 'ContactMessage', 'verbose_name_plural': 'ContactMessages'},
        ),
        migrations.AlterModelOptions(
            name='newsletter',
            options={'verbose_name': 'NewsLetter', 'verbose_name_plural': 'NewsLetters'},
        ),
    ]
