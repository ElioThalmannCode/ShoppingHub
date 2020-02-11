"""Django_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from pages import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path("contact/", views.contact_view),
    path('login/', views.login_view),
    path('products/', views.product_view),
    path('product/add/<int:num>/', views.add),
    path('products/<int:num>/', views.product_view_article),
    path('shoppingcart/', views.shoppingcart),
    path('product/delete/<int:num>/', views.delete),
    path('order/', views.order),
    path('email/', views.get_email),
    path('question/', views.send_question),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('about-us/', views.about_us),


    ]
admin.site.site_header = "ShoppingHub Admin by Elio Thalmann"
admin.site.site_title = "ShoppingHub Admin Portal"
admin.site.index_title = "Welcome to ShoppingHub Researcher Portal"