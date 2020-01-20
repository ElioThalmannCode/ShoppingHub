from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from blog.models import Product
from django.core.mail import send_mail
# Create your views here.
def home_view(request, *args, **kwargs):
    products =  Product.objects.all()
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
    return redirect("http://127.0.0.1:8000/shoppingcart/")

def shoppingcart(request, *args, **kwargs):
    scart = []
    total_price = 0
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
    return redirect("http://127.0.0.1:8000/shoppingcart/")



def order(request, *args, **kwargs):
    scart = []
    all_order = []
    for item in request.session.get("cart", [ ]):
        scart.append(Product.objects.get(id=item))
    for item in scart:
        all_order.append(item.title)
        all_order.append(f"{item.price}Fr.\n")
    all_order = '\n'.join(all_order)
    message = (f"""
Es hat jemand mit der Email {request.POST['your_email']}  hat bestellt.


Daten:

Anrede: {request.POST['your_se']}
sein Vorname: {request.POST['your_name']}
sein Nachname: {request.POST['your_lastname']}
seine PLZ: {request.POST['your_zip_code']}
sein Ort: {request.POST['your_ort']}
seine Adresse: {request.POST['your_adress']}
seine Adressnummer: {request.POST['your_adressnr']}
    
Produkte:
{all_order}
    """)
    message_client = (f"""
Du hast etwas bei Shoppinghub bestellt.


Daten:

Anrede: {request.POST['your_se']}
sein Vorname: {request.POST['your_name']}
sein Nachname: {request.POST['your_lastname']}
seine PLZ: {request.POST['your_zip_code']}
sein Ort: {request.POST['your_ort']}
seine Adresse: {request.POST['your_adress']}
seine Adressnummer: {request.POST['your_adressnr']}
    
bestellte Produkte:
{all_order}

Sie werden benachrichtigt wenn die Artikel geliefert wurden.
    """)
    send_mail(
        'order',
        message,
        'orders.shoppinghub@gmail.com',
        ['in19thel@tfbern.ch'],
        fail_silently=False,
    )
    send_mail(
        'order at shoppinghub',
        message_client,
        'orders.shoppinghub@gmail.com',
        [request.POST['your_email']],
        fail_silently=True,
    )
    return render(request, "order.html")

def get_email(request, *args, **kwargs):
    return render(request, "email.html")
def send_question(request, *args, **kwargs):
    send_mail(
        'shoppinghub',
        (f"""{request.POST['your_name']} mit der Email {request.POST['your_email']} hat dir folgende Nachricht geschrieben:
        
{request.POST['your_question']}
        """),
        'orders.shoppinghub@gmail.com',
        ["in19thel@tfbern.ch"],
        fail_silently=True,
    )






