from django import forms
from Servicio.models import Producto,Marca

class ProductoForm(forms.ModelForm):

    nombre=forms.CharField(min_length=3,max_length=50)
    imagen=forms.ImageField(required=False)
    precio=forms.IntegerField(min_value=1,max_value=100000000,)

    class Meta:
        model=Producto
        #fields=["nombre","correo",.....]
        fields='__all__'