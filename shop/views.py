from django.shortcuts import render, get_object_or_404
from . models import Category, Product
from cart.forms import CartAddProductForm


def index(request):
    return render(request, 'shop/index.html')


def contact(request):
    return render(request, 'shop/contact-us.html')


# def shoping(request, category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     products = Product.objects.filter(available=True)
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         products = products.filter(category=category)
#     return render(request, 'shop/shop.html',
#                   {'category': category,
#                    'categories': categories,
#                    'products': products})


def shop(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    productt = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        productt = productt.filter(category=category)
    return render(request, 'shop/shop.html',
                  {'category': category,
                   'categories': categories,
                   'productt': productt})


def product_details(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product_details.html', {'product': product,
                                                         'cart_product_form': cart_product_form})


def shop_grid(request):
    return render(request, 'shop/shop-grid-right-sidebar.html')


def shop_list(request):
    return render(request, 'shop/shop-list-right-sidebar.html')


def wishlist(request):
    return render(request, 'shop/wishlist.html')


def cart(request):
    return render(request, 'shop/cart.html')


def checkout(request):
    return render(request, 'shop/checkout.html')