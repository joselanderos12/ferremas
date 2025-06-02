from django.urls import path
from . import views

urlpatterns =[
    path('', views. home, name='home'),

    path('contacto/', views. contacto, name='contacto'),  
    path('catalogo/', views. catalogo, name='catalogo'),
    path('login/', views. login, name='login'),
    path('registro/', views. registro, name='registro'),
    path('carrito/', views. carrito, name='carrito'),
    path('producto_del/<str:pk>', views.producto_del, name='producto_del'),
    path('agregar_producto', views.agregar_producto, name='agregar_producto'),
]