from django.shortcuts import render
from Servicio.models import Producto,Marca
from Servicio.forms import ProductoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required,permission_required


# Create your views here.
@login_required
@permission_required('Servicio.add_producto')
def servicio(request):
    servicios=Producto.objects.all()
    data={
        'form':ProductoForm(),
        "servicios":servicios,
       
    }
    if request.method=="POST":
        formulario=ProductoForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Agregado")
            #data["mensaje"]="producto guardado"
        else:
            data["form"]=formulario

    return render(request,"Servicio/servicio.html",data)