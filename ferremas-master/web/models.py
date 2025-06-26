from django.db import models

# Create your models here.


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen_url = models.URLField(default='https://ejemplo.com/imagen-default.jpg')  
    
    def __str__(self):
        return self.nombre
