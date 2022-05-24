from django import forms
from app.models import * 
from django.forms import inlineformset_factory  

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('nome','desc')
class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ('tamanho','preco')
class BebidaForm(forms.ModelForm):
    class Meta:
        model = Bebida
        fields = ('tamanho','preco','quant')

PizzaFormset = inlineformset_factory(Produto,Pizza,fields = ('tamanho','preco'), extra=4,max_num=4,can_delete=True)
BebidaFormset = inlineformset_factory(Produto,Bebida,fields = ('tamanho','preco','quant'), extra=4,max_num=4,can_delete=True)
        