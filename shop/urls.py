from django.urls import path, include
from .views import *
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='main'),
    path('shop/', views.shop, name='shop'),
    path('contact-us', views.contact, name='contact'),
    # path('<slug:category_slug>/', views.shoping, name='shoping'),
    path('int:id>/<slug:slug', views.product_details, name='product_details'),
    path('shop_grid/', views.shop_grid, name='shop_grid'),
    path('shop_list/', views.shop_list, name='shop_list'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    ]
