from django import forms

class Formulario_Insumos (forms.Form):
    tipo= forms.CharField ()
    marca= forms.CharField ()
    stock= forms.IntegerField ()


