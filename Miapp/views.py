from http.client import HTTPResponse
from this import d
from django.shortcuts import render, redirect
from django.template import Context, Template
from Miapp.forms import Formulario_Insumos, Formulario_celulares, Formulario_hardware, Formulario_software
from .models import Celulares, Insumos,Hardware,Software

# Create your views here.

def inicio (request):
    return render(request,"inicio.html")

def celulares (request):
    return render (request, "lista_celulares.html")

def hardware (request):
    return render(request, "lista_hardware.html")

def software (request):
    return render(request, "lista_software.html")

def insumos (request):
    return render (request, "lista_insumos.html")

def agregado (request):
    return render (request, "agregado.html")

def formulario_insumo (request):
    if request.method == "POST":
        mi_formulario = Formulario_Insumos (request.POST)
        if mi_formulario.is_valid():
            data= mi_formulario.cleaned_data
            formulario = Insumos (tipo_insumo=data ['tipo'], marca_insumo= data ['marca'], stock_insumo= data ['stock'])
            formulario.save()
            return redirect ("agregado")
    else:
            mi_formulario = Formulario_Insumos ()
    return render (request, "formulario_insumo.html", {'mi_formulario': mi_formulario})

def formulario_software (request):
    if request.method == "POST":
        mi_formulario = Formulario_software (request.POST)
        if mi_formulario.is_valid():
            data= mi_formulario.cleaned_data
            formulario = Software (tipo_software=data ['tipo'], marca_software= data ['marca'], stock_software= data ['stock'])
            formulario.save()
            return redirect ("agregado")
    else:
            mi_formulario = Formulario_software ()
    return render (request, "formulario_software.html", {'mi_formulario': mi_formulario})

def formulario_hardware (request):
    if request.method == "POST":
        mi_formulario = Formulario_hardware (request.POST)
        if mi_formulario.is_valid():
            data= mi_formulario.cleaned_data
            formulario = Hardware (tipo_hardware=data ['tipo'], marca_hardware = data ['marca'], stock_hardware= data ['stock'])
            formulario.save()
            return redirect ("agregado")
    else:
            mi_formulario = Formulario_hardware ()
    return render (request, "formulario_hardware.html", {'mi_formulario': mi_formulario})

def formulario_celulares (request):
    if request.method == "POST":
        mi_formulario = Formulario_celulares (request.POST)
        if mi_formulario.is_valid():
            data= mi_formulario.cleaned_data
            formulario = Celulares (marca_celular=data ['marca'], modelo_celular= data ['modelo'], stock_celular= data ['stock'])
            formulario.save()
            return redirect ("agregado")
    else:
            mi_formulario = Formulario_celulares ()
    return render (request, "formulario_celulares.html", {'mi_formulario': mi_formulario})