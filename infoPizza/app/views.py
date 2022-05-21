from pyexpat import model
from django.shortcuts import render, redirect 
  
from app.forms import * 
from app.models import *
import logging

def index(request) :
    return render(request,'index.html')

def cardapioIndex(request) :
    return render(request,'cardapio/index.html') 

def cardapioPizzaIndex(request) :
    pizzas = Item.objects.filter(cat__iexact='1')  
    return render(request,"cardapio/pizza/index.html",{'pizzas':pizzas}) 

def cardapioPizzaInsert(request) :
    novaPizza = Item()
    if request.method == "POST":
        form = ItemForm(request.POST,request.FILES,instance=novaPizza,prefix='form')
        form2 = ItemFormset(request.POST,request.FILES,instance=novaPizza,prefix='form2')
        if form.is_valid() and form2.is_valid():  
            try:  
                form.save()
                form2.save()
                return redirect('/cardapio/pizza')  
            except:  
                pass  
    else:  
        form = ItemForm({'form-cat':'1'},instance=novaPizza,prefix='form')
        form2 = ItemFormset(instance=novaPizza,prefix='form2')
    return render(request,'cardapio/pizza/insert.html',{'form':form,'form2':form2})  



def cardapioPizzaUpdate(request, id):  
    pizza = Item.objects.get(id=id)
    if request.method == 'POST':
        form = ItemForm(request.POST,request.FILES,instance=pizza,prefix='form')
        form2 = ItemFormset(request.POST,request.FILES,instance=pizza,prefix='form2')
        logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
        logging.debug('form=%s', pizza.id)
        if form.is_valid() and form2.is_valid():  
            try:  
                form.save()
                form2.save()
                return redirect('/cardapio/pizza')  
            except:  
                pass
    else:
        form = ItemForm(instance=pizza,prefix='form')
        form2 = ItemFormset(instance=pizza,prefix='form2')
    return render(request, 'cardapio/pizza/edit.html', {'form':form,'form2':form2,'pizza':pizza})  

def cardapioPizzaDestroy(request, id):  
    pizza = Item.objects.get(id=id)  
    pizza.delete()  
    return redirect("/cardapio/pizza")

def cardapioBebidaIndex(request) :
    bebidas = Item.objects.filter(cat__iexact='2')  
    return render(request,"cardapio/bebida/index.html",{'bebidas':bebidas}) 

def cardapioBebidaInsert(request) :
    if request.method == "POST":  
        form = ItemForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/cardapio/bebida')  
            except:  
                pass  
    else:  
        form = ItemForm({'cat':'2'})  
    return render(request,'cardapio/bebida/insert.html',{'form':form})  

def cardapioBebidaEdit(request,id) :
    bebida = Item.objects.get(id=id)  
    return render(request,'cardapio/bebida/edit.html', {'bebida':bebida})

def cardapioBebidaUpdate(request, id):  
    bebida = Item.objects.get(id=id)  
    form = ItemForm(request.POST, instance = bebida)  
    if form.is_valid():  
        form.save()  
        return redirect("/cardapio/bebida")  
    return render(request, 'cardapio/bebida/edit.html', {'bebida': bebida})  

def cardapioBebidaDestroy(request, id):  
    bebida = Item.objects.get(id=id)  
    bebida.delete()  
    return redirect("/cardapio/bebida")

def pedidosIndex(request) :
    mesas = Mesa.objects.all
    return render(request,'pedidos/index.html',{'mesas':mesas}) 
    
def pedidosMesaOrder(request,id) :
    if request.method == "POST":  
        form = PedidoForm(request.POST)
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/pedidos/mesa')  
            except:  
                pass  
    else:  
        form = PedidoForm()
    return render(request,'pedidos/mesa/order.html',{'form':form})

def caixaMesaInsert(request) :
    Mesa.objects.create()
    return redirect('/pedidos')
  
