from http.client import HTTPResponse
from django.shortcuts import render
from django.template import Context, Template
from .models import Celulares,Insumos,Hardware,Software

# Create your views here.

def inicio (request):
    return render(request,"inicio.html")
    
def celulares (request):
    return render(request, "lista_celulares.html")

def hardware (request):
    return render(request, "lista_hardware.html")

def software (request):
    return render(request, "lista_software.html")

def insumos (request):
    return render (request, "lista_insumos.html")

def formulario_insumo (request):
    if request.method == "POST":
        mi_formulario = Insumos (request.POST)
        if mi_formulario.is_valid():
            data=mi_formulario.cleaned_data
            formulario = Insumos (tipo_insumo=data ['tipo de insumo'], marca_insumo= data ['marca'], 
            stock_insumo= data ['cantidad a ingresar'])
            formulario.save()
            return redirect ("insumos")
    else:
            mi_formulario = Insumos ()
    return render (request, "formulario_insumo.html", {'mi_formulario': mi_formulario})
