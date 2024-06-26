# Generated by Django 4.2.2 on 2023-07-10 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshop', '0003_rename_dishes_dish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='image',
            field=models.ImageField(upload_to='onlineshop/images'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(upload_to='onlineshop/images'),
        ),
    ]
