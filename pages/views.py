from django.shortcuts import render
from django.shortcuts import HttpResponse
from blog.models import Product
# Create your views here.
def home_view(request, *args, **kwargs):
    products =  Product.objects.all()
    print(products)
    return render(request, "home.html",  {"products": products})
def contact_view(request, *args, **kwargs):
    return render(request, "contact.html")
def login_view(request, *args, **kwargs):
    return render(request, "login.html")

def product_view(request, *args, **kwargs):
    products =  Product.objects.all()
    return render(request, "product.html", {"products": products})

def product_view_article(request, *args, **kwargs):
    product =  Product.objects.get(id=kwargs.get("num"))
    return render(request, "product_view_article.html", {"product": product})

def add(request, num, *args, **kwargs):
    scart = []
    product = Product.objects.get(id=num)
    cart = request.session.get("cart", [ ])
    cart.append(product.id)
    request.session['cart'] = cart
    for id in request.session.get("cart", [ ]):
        scart.append(Product.objects.get(id=id))
    return render(request, "shoppingcart.html", {"shopping_cart": scart})

def shoppingcart(request, *args, **kwargs):
    scart = []
    #print(request.session.get("cart", [ ]))
    for id in request.session.get("cart", [ ]):
        scart.append(Product.objects.get(id=id))
    #product =  Product.objects.get(request.session.get("cart", [ ]))
    return render(request, "shoppingcart.html", {"shopping_cart": scart})

def delete(request, num, *args, **kwargs):
    scart = []
    product = Product.objects.get(id=num)
    cart = request.session.get("cart", [ ])
    cart.remove(product.id)
    request.session['cart'] = cart
    for id in request.session.get("cart", [ ]):
        scart.append(Product.objects.get(id=id))
    return render(request, "shoppingcart.html", {"shopping_cart": scart})

