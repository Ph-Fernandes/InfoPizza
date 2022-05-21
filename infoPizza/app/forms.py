from django import forms
from app.models import * 
from django.forms import inlineformset_factory  

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = "__all__"
class PizzaInfoForm(forms.ModelForm):
    class Meta:
        model = PizzaInfo
        fields = ('tamanho','preco')
class BebidaForm(forms.ModelForm):
    class Meta:
        model = Bebida
        fields = "__all__"
class BebidaInfoForm(forms.ModelForm):
    class Meta:
        model = BebidaInfo
        fields = ('tamanho','preco')

PizzaFormset = inlineformset_factory(Pizza,PizzaInfo,form=PizzaInfoForm, extra=4,max_num=4)
BebidaFormset = inlineformset_factory(Bebida,BebidaInfo,form=BebidaInfoForm, extra=4,max_num=4)
        