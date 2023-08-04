
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('restaurant_login/',views.restaurant_login,name='restaurant_login'),
    path('restaurant_signup/',views.restaurant_signup,name='restaurant_signup'),
    path('signup/',views.signup,name='signup'),
    path('home/',views.home,name='home'),
    path('restaurant_home/',views.restaurant_home,name='restaurant_home'),
    path('logout/',views.logout,name='logout'),
    path('add_dish/',views.add_dish,name='add_dish'),
    path('restaurant_logout/',views.restaurant_logout,name='restaurant_logout'),
    path('edit_dish/<int:dish_id>/', views.edit_dish, name='edit_dish'),
    path('checkout/',views.checkout,name='check out'),
    path('restaurants/', views.restaurant_detail, name='restaurant_detail'),
    path('admin/', admin.site.urls),
]
