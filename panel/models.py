from django.db import models

class Emprendimiento(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Emprendimiento")
    dueño = models.CharField(max_length=100, verbose_name="Nombre del Dueño")
    lugar = models.CharField(max_length=200, verbose_name="Ubicación")
    descripcion = models.TextField(verbose_name="Descripción")
    productos = models.TextField(verbose_name="Productos que ofrece")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre



# Create your models here.
