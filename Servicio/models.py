from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()
    descripcion=models.TextField()
    imagen=models.ImageField(upload_to='Productos', null=True, blank=True)
    nuevo=models.BooleanField()
    fecha_fabricado=models.DateField()
    marca=models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre