from django import forms

class Formulario_Insumos (forms.Form):
    tipo_insumo= forms.CharField ()
    marca_insumo= forms.CharField ()
    stock_insumo= forms.IntegerField ()


