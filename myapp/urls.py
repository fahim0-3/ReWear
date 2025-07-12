"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    
    path('about', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:id>/', views.blog_details, name='blog_details'),
    path('checkout', views.checkout, name='checkout'),
    path('contact', views.contact, name='contact'),
    path('', views.index, name='index'),
    path('main', views.main, name='main'),
    path('shop/<int:product_id>/<str:main_category_id>', views.shop_details, name='shop_details'),
    path('add_cart/<int:id>', views.add_cart, name='add_cart'),
    path('cart_delete/<int:id>', views.cart_delete, name='cart_delete'),
    path('cart_plus/<int:id>', views.cart_plus, name='cart_plus'),
    path('cart_minus/<int:id>', views.cart_minus, name='cart_minus'),
    path('shop', views.shop, name='shop'),
    path('shopping_cart', views.shopping_cart, name='shopping_cart'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('forgot', views.forgot, name='forgot'),
    path('conform', views.conform, name='conform'),
    path('search_fun', views.search_fun, name='search_fun'),
    path('apply_coupon', views.apply_coupon, name='apply_coupon'),
    path('billing_details', views.billing_details, name='billing_details'),
    path('add_to_wishlist/<int:id>', views.add_to_wishlist, name='add_to_wishlist'),

]
