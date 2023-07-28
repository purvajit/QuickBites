from django.db import models

# Create your models here.

class city(models.Model):
    city_id = models.AutoField
    city_name = models.CharField(max_length=50)

    def __str__(self):
        return self.city_name


class restaurant(models.Model):
    restaurant_id = models.AutoField
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    address = models.CharField(max_length=400)
    city = models.ForeignKey(city, on_delete=models.CASCADE)
    zip_code = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    image = models.ImageField(upload_to='onlineshop/images')
    password = models.CharField(max_length=50)


    def __str__(self):
        return self.name

class dish(models.Model):
    dish_id = models.AutoField
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    price = models.PositiveIntegerField()
    restaurant_id = models.ForeignKey(restaurant, on_delete=models.CASCADE)
    spiciness_Level = models.CharField(max_length=10)
    image = models.ImageField(upload_to='onlineshop/images')

    def __str__(self):
        return self.name

class user(models.Model):
    user_id = models.AutoField
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=400)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=6)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username
