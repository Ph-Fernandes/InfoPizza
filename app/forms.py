from asyncio.windows_events import NULL
from cProfile import label
from dataclasses import field, fields
from tkinter import Label
from app.models import *  
from django.forms import ChoiceField, ModelChoiceField, inlineformset_factory  
from django.db.models.fields import BLANK_CHOICE_DASH
from django import forms  
from localflavor.br.forms import BRCPFField,BRZipCodeField
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

import logging


# cadastro PIZZA E BEBIDA
class ProdutoForm(forms.ModelForm):
    nome = forms.CharField(label='Nome')
    desc = forms.CharField(widget=forms.Textarea, label='Descrição')
    class Meta:
        model = Produto
        fields = ('nome','desc')

class PizzaForm(forms.ModelForm):
    tamanho = forms.ChoiceField(choices= BLANK_CHOICE_DASH + [("B","B"),("M","M"),("G","G"),("GG","GG")], label='Tamanho')
    preco = forms.DecimalField(label='Preço')
    class Meta:
        model = ProdutoInfo
        fields = ('tamanho','preco')

class BebidaForm(forms.ModelForm):
    tamanho = forms.ChoiceField(choices= BLANK_CHOICE_DASH + [("350ml","350ml"),("600ml","600ml"),("1000ml","1000ml"),("1500ml","1500ml"),("2000ml","2000ml")], label='Tamanho')
    preco = forms.DecimalField(label='Preço')
    class Meta:
        model = ProdutoInfo
        fields = ('tamanho','preco')


PizzaFormset = inlineformset_factory(Produto, ProdutoInfo, form=PizzaForm,  extra=4, max_num=4,  can_delete=True)
BebidaFormset = inlineformset_factory(Produto ,ProdutoInfo, form=BebidaForm,  extra=5, max_num=5, can_delete=True)

# PEDIDO
class PedidoChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.nome+" "+obj.sobrenome+" ("+obj.cpf+")" 

class PedidoForm(forms.ModelForm):
    obs = forms.CharField(required=False)
    cliente = PedidoChoiceField(
        widget=forms.Select,
        queryset = Cliente.objects.all(),
        to_field_name='id',
        empty_label="Nenhum"
    )
    metodoPag = forms.ChoiceField(
        choices = BLANK_CHOICE_DASH + [('Dinheiro','Dinheiro'),('Pix','Pix'),('Cartão de Crédito/Debito','Cartão de Crédito/Debito'),('PicPay','PicPay'),('Mercado Pago', 'Mercado Pago'),('Ame Digital', 'Ame Digital')]) 
    class Meta:
        model = Pedido
        exclude = ('cat','status','tempo')

    def __init__(self, *args, **kwargs):
        super(PedidoForm, self).__init__(*args, **kwargs)
        self.fields['total'].widget.attrs['readonly'] = True
        if self.instance.cat == 2:
            self.fields['cliente'].required = False
            self.fields['metodoPag'].required = False

class PedidoForm2(forms.ModelForm):
    status = ChoiceField()
    obs = forms.CharField(required=False)
    metodoPag = forms.ChoiceField(
        choices = BLANK_CHOICE_DASH + [('Dinheiro','Dinheiro'),('Pix','Pix'),('Cartão de Crédito/Debito','Cartão de Crédito/Debito'),('PicPay','PicPay'),('Mercado Pago', 'Mercado Pago'),('Ame Digital', 'Ame Digital')])
    class Meta:
        model = Pedido
        exclude = ('cat','cliente','tempo')
    def __init__(self, *args, **kwargs):
        super(PedidoForm2, self).__init__(*args, **kwargs)
        self.fields['total'].widget.attrs['readonly'] = True
        if self.instance.cat == 1:
            self.fields['status'].choices = [
                ('Anotado','Anotado'),
                ('Preparando','Preparando'),
                ('Cancelado','Cancelado'),
                ('Pedido Pronto','Pedido Pronto'),
                ('Saiu para entrega','Saiu para entrega'),
                ('Finalizado','Finalizado')]
        else:
            self.fields['status'].choices = [
                ('Anotado','Anotado'),
                ('Preparando','Preparando'),
                ('Cancelado','Cancelado'),
                ('Pedido Pronto', 'Pedido Pronto'),
                ('Servido','Servido'),
                ('Finalizado','Finalizado')]
            self.fields['metodoPag'].required = False
            
class ItensChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.nome

class ItensPedidoForm(forms.ModelForm):
    produto = ItensChoiceField(
        widget=forms.Select,
        queryset = Produto.objects.all().filter(cat=1),
        to_field_name='id',
        empty_label="Escolha"
    )

    tamanho = forms.ModelChoiceField(
        widget=forms.Select,
        queryset=ProdutoInfo.objects.none(),
        empty_label="Escolha",
    )

    def __init__(self, *args, **kwargs):
        super(ItensPedidoForm, self).__init__(*args, **kwargs)
        self.fields['preco'].widget.attrs['readonly'] = True
        if self.data != {}:
            self.fields['tamanho'].queryset = ProdutoInfo.objects.all()
    
    class Meta:
        model = ItensPedido
        fields = '__all__'

class ItensPedidoForm2(forms.ModelForm):
    produto = ItensChoiceField(
        widget=forms.Select,
        queryset = Produto.objects.all().filter(cat=2),
        to_field_name='id',
        empty_label="Escolha"
    )

    tamanho = forms.ModelChoiceField(
        widget=forms.Select,
        queryset=ProdutoInfo.objects.none(),
        empty_label="Escolha",
    )

    def __init__(self, *args, **kwargs):
        super(ItensPedidoForm2, self).__init__(*args, **kwargs)
        self.fields['preco'].widget.attrs['readonly'] = True
        if self.data != {}:
            self.fields['tamanho'].queryset = ProdutoInfo.objects.all()
                
    class Meta:
        model = ItensPedido
        fields = '__all__'

PedidoPizzaFormset = inlineformset_factory(Pedido, ItensPedido, form=ItensPedidoForm, extra=1, max_num=20, can_delete=True)
PedidoBebidaFormset = inlineformset_factory(Pedido, ItensPedido, form=ItensPedidoForm2, extra=1, max_num=20, can_delete=True)

# CLIENTE

class clienteForm(forms.ModelForm):
    cpf = BRCPFField(label='CPF')
    dtnasc = forms.DateField(
        widget=forms.SelectDateWidget(years=range(1922, 2022)), 
        label='Data de Nascimento')
    telefone = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(initial='BR')
        )
    cep = BRZipCodeField(label='CEP') 
    class Meta:
        model = Cliente
        exclude = ['cadastro']

# MESA

class MesaChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.id

class mesaForm(forms.ModelForm):
    id = MesaChoiceField(
        widget=forms.Select,
        queryset=Mesa.objects.filter(pedido=None),
        to_field_name='id',
        empty_label="Escolha",
    )
    class Meta:
        model = Mesa
        #fields = '__all__'
        exclude = ['pedido']


# CAIXA

class caixaForm(forms.ModelForm):
    obs = forms.CharField(required=False)
    metodoPag = forms.ChoiceField(
        choices = BLANK_CHOICE_DASH + [('Dinheiro','Dinheiro'),('Pix','Pix'),('Cartão de Crédito/Debito','Cartão de Crédito/Debito'),('PicPay','PicPay'),('Mercado Pago', 'Mercado Pago'),('Ame Digital', 'Ame Digital')])
    
    class Meta:
        model = Pedido
        fields = ('obs', 'metodoPag', 'total')
