
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
    # path('shop/',views.shop,name='shop'),
    # path('partner-with-us/',views.partner_with_us,name='partner'),
    # path('search/',views.search,name='search'),
    # path('restaurants/',views.restaurants,name='restaurants'),
    # path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='check out'),
    path('restaurants/', views.restaurant_detail, name='restaurant_detail'),
    path('admin/', admin.site.urls),
]
