# Generated by Django 4.2.2 on 2023-07-10 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshop', '0002_restaurant_image_dishes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='dishes',
            new_name='dish',
        ),
    ]
