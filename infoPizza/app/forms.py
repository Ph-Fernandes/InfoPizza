from django import forms
from app.models import * 
from django.forms import inlineformset_factory  

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"
class ItemInfoForm(forms.ModelForm):
    class Meta:
        model = ItemInfo
        fields = ('tamanho','preco')

ItemFormset = inlineformset_factory(Item, ItemInfo,form=ItemInfoForm, extra=4,max_num=4)
        
class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = "__all__"
class MesaForm(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = "__all__"