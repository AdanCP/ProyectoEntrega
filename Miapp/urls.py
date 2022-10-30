from django.urls import path
from .models import Hardware, Software, Insumos, Celulares
from .views import agregado, celulares, formulario_insumo, hardware, inicio, formulario_insumo, insumos,software


urlpatterns = [
    path("", inicio,name='Inicio'),
    path ("lista_celulares/", celulares,name='Celulares'),
    path ("lista_hardware/", hardware,name='Hardware'),
    path ("lista_insumos/", insumos,name='Insumos'),
    path ("lista_software/", software,name='Software'),
    path ("formulario_insumo/", formulario_insumo, name='Formulario_insumo'),
    path ("agregado/", agregado, name = "agregado"),
]
