from django.db import models

# Create your models here.

class Producto (models.Model):
    nombre = models.CharField(max_length=500, blank= True)
    descripcion = models.TextField(max_length=2000, blank=True)
    precio = models.DecimalField(max_digits=4, decimal_places=2)
    fecha_de_ingreso = models.DateTimeField(auto_now_add=True)

    def _str_ (self):
        return self.nombre
