from django.db import models

# Create your models here.

class Producto (models.Model):
    nombre = models.CharField(max_length=100, blank=False, verbose_name="Nombre : " , help_text="introdusca solo valores de caracteres",editable=True)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_de_ingreso = models.DateTimeField(auto_now_add=True)

    def _str_ (self):
        return self.nombre
