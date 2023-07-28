# Generated by Django 4.2.2 on 2023-07-11 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshop', '0005_user_rename_state_restaurant_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='city',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlineshop.city'),
        ),
    ]