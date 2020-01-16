from django.shortcuts import render
from django.shortcuts import HttpResponse
from blog.models import Product
from django.core.mail import send_mail
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
    total_price = 0
    #print(request.session.get("cart", [ ]))
    for id in request.session.get("cart", [ ]):
        product  = Product.objects.get(id=id)
        total_price += product.price
        scart.append(product)
    return render(request, "shoppingcart.html", {
        "shopping_cart": scart,
        "total_price": total_price
        })

def delete(request, num, *args, **kwargs):
    scart = []
    product = Product.objects.get(id=num)
    cart = request.session.get("cart", [ ])
    cart.remove(product.id)
    request.session['cart'] = cart
    for id in request.session.get("cart", [ ]):
        scart.append(Product.objects.get(id=id))
    return render(request, "shoppingcart.html", {"shopping_cart": scart})



def order(request, *args, **kwargs):
    send_mail(
        'order',
        'ok cool',
        'orders.shoppinghub@gmail.com',
        ['in19thel@tfbern.ch'],
        fail_silently=True,
    )
    return render(request, "order.html")






