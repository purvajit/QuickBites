# Generated by Django 4.2.2 on 2023-07-25 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshop', '0009_alter_user_password_alter_user_zip_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]