# Generated by Django 3.0.5 on 2020-04-25 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200425_1136'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='catergory',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='subcatergory',
            new_name='subcategory',
        ),
    ]
