from django.shortcuts import render,HttpResponse,redirect, get_object_or_404
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required,permission_required

# Create your views here.

def home(request):
    return render(request,"PruebaApp/home.html")

def registro(request):
    data={
        "form":CustomUserCreationForm(),
    }
    if request.method=="POST":
        formulario=CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user=authenticate(
            username=formulario.cleaned_data["username"],
            password=formulario.cleaned_data["password1"]
            )
            login(request,user)
            messages.success(request,"Te has registrado correctamente")
            return redirect(to='home')
        else:
            data["form"]=formulario

    return render(request,'registration/registro.html',data)