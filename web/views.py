from django.http import JsonResponse
from django.shortcuts import render, redirect,get_object_or_404
from .models import Producto
import json

# Create your views here.

def home(request): 
    context={}
    return render(request,'web/home.html', context)

def login(request):
    return render(request, 'web/login.html')

def contacto(request):
    return render(request, 'web/contacto.html')


def registro(request):
    return render(request, 'web/registro.html')

def carrito(request):
    productos= Producto.objects.all()
    context= {'productos':productos}
    return render(request, 'web/carrito.html', context)



def catalogo(request):
    return render(request, 'web/catalogo.html')

def agregar_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        imagen_url = request.POST.get('imagen_url')
        
        producto = Producto(nombre=nombre, descripcion=descripcion, precio=precio, imagen_url=imagen_url)
        producto.save()
        
        return redirect('catalogo')
    return render(request, 'web/catalogo.html', {'mensaje': 'Producto agregado correctamente.'})  


def producto_del(request, pk):
    context = {}
    try:
        producto = Producto.objects.get(id=pk)
        producto.delete()

        mensaje = "Producto eliminado correctamente"
        productos = Producto.objects.all()
        context = {'productos': productos, 'mensaje': mensaje}
    except Producto.DoesNotExist:
        mensaje = "El producto no existe"
        productos = Producto.objects.all()
        context = {'productos': productos, 'mensaje': mensaje}
    except Exception as e:
        mensaje = f"Error al eliminar el producto: {str(e)}"
        productos = Producto.objects.all()
        context = {'productos': productos, 'mensaje': mensaje}

    return render(request, 'web/carrito.html', context)













#APIs:
#def api_productos(request):
    productos = Producto.objects.all()
    data = [{
        'id': p.id,
        'nombre': p.nombre,
        'descripcion': p.descripcion,
        'precio': p.precio,
        'stock': p.stock
    } for p in productos]
    return JsonResponse(data, safe=False)


#@csrf_exempt
#def api_usuarios(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # Crear usuario
        usuario = Usuario.objects.create(**data)
        return JsonResponse({'success': True})

    usuarios = Usuario.objects.all()
    data = [{'id': u.id, 'nombre': u.nombre, 'correo': u.correo} for u in usuarios]
    return JsonResponse(data, safe=False)
