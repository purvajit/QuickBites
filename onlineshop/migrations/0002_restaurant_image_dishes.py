# Generated by Django 4.2.2 on 2023-07-10 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='image',
            field=models.CharField(default=0, max_length=300),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='dishes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
                ('price', models.PositiveIntegerField()),
                ('spiciness_Level', models.CharField(max_length=10)),
                ('image', models.CharField(max_length=300)),
                ('restaurant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlineshop.restaurant')),
            ],
        ),
    ]