from django.shortcuts import render

# Create your views here.

def home(request): 
    context={}
    return render(request,'web/home.html', context)


def catalogo(request):
    productos = [
        {
            'nombre': 'Taladro Inalámbrico Bosch',
            'imagen': 'web/media/2.png',
            'precio': 89990,
            'descripcion': 'Potente taladro inalámbrico de 18V ideal para trabajos pesados.'
        },
        {
            'nombre': 'Juego de Llaves Allen',
            'imagen': 'web/media/5.png',
            'precio': 12990,
            'descripcion': 'Set de llaves Allen de acero reforzado.'
        },
        {
            'nombre': 'Pintura Látex Interior 1 Galón',
            'imagen': 'web/media/6.png',
            'precio': 21990,
            'descripcion': 'Pintura blanca de alta cobertura para interiores.'
        }
    ]
    return render(request, 'web/catalogo.html', {'productos': productos})


def login(request):
    return render(request, 'web/login.html')

def contacto(request):
    return render(request, 'web/contacto.html')


def registro(request):
    return render(request, 'web/registro.html')

def carrito(request):
    return render(request, 'web/carrito.html')
