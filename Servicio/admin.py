from django.contrib import admin
from Servicio.models import Marca,Producto

# Register your models here.

class MarcaAdmin(admin.ModelAdmin):
    list_display=("nombre",)

    
admin.site.register(Marca,MarcaAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display=("nombre","precio","descripcion")

    
admin.site.register(Producto,ProductoAdmin)
