from django.urls import path
from . import views

urlpatterns =[
    path('home', views. home, name='home'),

    path('contacto/', views. contacto, name='contacto'),  
    path('catalogo/', views. catalogo, name='catalogo'),
    path('login/', views. login, name='login'),
    path('registro/', views. registro, name='registro'),
    path('carrito/', views. carrito, name='carrito'),
]