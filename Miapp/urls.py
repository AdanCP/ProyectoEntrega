from django.urls import path
from .models import Hardware, Software, Insumos, Celulares
from .views import agregado, celulares, formulario_celulares, formulario_hardware, formulario_insumo, formulario_software, formulario_software, hardware, inicio, formulario_insumo, insumos,software


urlpatterns = [
    path("", inicio,name='Inicio'),
    path ("lista_hardware/", hardware,name='Hardware'),
    path ("lista_insumos/", insumos,name='Insumos'),
    path ("lista_software/", software,name='Software'),
    path ("formulario_insumo/", formulario_insumo, name='Formulario_insumo'),
    path ("formulario_software/", formulario_software, name='Formulario_software'),
    path ("formulario_hardware/", formulario_hardware, name='Formulario_hardware'),
    path ("formulario_celulares/", formulario_celulares, name= 'Formulario_celulares'),
    path ("agregado/", agregado, name = "agregado"),
]
