from django.contrib import admin

# Register your models here.
from .models import restaurant,dish,user,city

admin.site.register(restaurant)
admin.site.register(dish)
admin.site.register(user)
admin.site.register(city)