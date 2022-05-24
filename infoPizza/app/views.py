from pyexpat import model
from django.shortcuts import render, redirect 
  
from app.forms import * 
from app.models import *

def index(request) :
    return render(request,'index.html')

def cardapioIndex(request) :
    return render(request,'cardapio/index.html') 

def cardapioPizzaIndex(request) :
    pizzas = Produto.objects.filter(cat__iexact=1)
    return render(request,"cardapio/pizza/index.html",{'pizzas':pizzas}) 

def cardapioPizzaInsert(request) :
    novaPizza = Produto(cat=1)
    if request.method == "POST":
        form = ProdutoForm(request.POST,request.FILES,instance=novaPizza,prefix='form')
        form2 = PizzaFormset(request.POST,request.FILES,instance=novaPizza,prefix='form2')
        if form.is_valid() and form2.is_valid():  
            try:  
                form.save()
                form2.save()
                return redirect('/cardapio/pizza')  
            except:  
                pass  
    else:  
        form = ProdutoForm(instance=novaPizza,prefix='form')
        form2 = PizzaFormset(instance=novaPizza,prefix='form2')
    return render(request,'cardapio/pizza/insert.html',{'form':form,'form2':form2})  



def cardapioPizzaUpdate(request, id):  
    pizza = Produto.objects.get(id=id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST,request.FILES,instance=pizza,prefix='form')
        form2 = PizzaFormset(request.POST,request.FILES,instance=pizza,prefix='form2')
        if form.is_valid() and form2.is_valid():  
            try:  
                form.save()
                form2.save()
                return redirect('/cardapio/pizza')  
            except:  
                pass
    else:
        form = ProdutoForm(instance=pizza,prefix='form')
        form2 = PizzaFormset(instance=pizza,prefix='form2')
    return render(request, 'cardapio/pizza/edit.html', {'form':form,'form2':form2,'pizza':pizza})  

def cardapioPizzaDestroy(request, id):  
    pizza = Produto.objects.get(id=id)  
    pizza.delete()  
    return redirect("/cardapio/pizza")


def cardapioBebidaIndex(request) :
    bebidas = Produto.objects.filter(cat__iexact=2)
    return render(request,"cardapio/bebida/index.html",{'bebidas':bebidas}) 

def cardapioBebidaInsert(request) :
    novaBebida = Produto(cat=2)
    if request.method == "POST":
        form = ProdutoForm(request.POST,request.FILES,instance=novaBebida,prefix='form')
        form2 = BebidaFormset(request.POST,request.FILES,instance=novaBebida,prefix='form2')
        if form.is_valid() and form2.is_valid():  
            try:  
                form.save()
                form2.save()
                return redirect('/cardapio/bebida')  
            except:  
                pass  
    else:  
        form = ProdutoForm(instance=novaBebida,prefix='form')
        form2 = BebidaFormset(instance=novaBebida,prefix='form2')
    return render(request,'cardapio/bebida/insert.html',{'form':form,'form2':form2})  



def cardapioBebidaUpdate(request, id):  
    bebida = Produto.objects.get(id=id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST,request.FILES,instance=bebida,prefix='form')
        form2 = BebidaFormset(request.POST,request.FILES,instance=bebida,prefix='form2')
        if form.is_valid() and form2.is_valid():  
            try:  
                form.save()
                form2.save()
                return redirect('/cardapio/bebida')  
            except:  
                pass
    else:
        form = ProdutoForm(instance=bebida,prefix='form')
        form2 = BebidaFormset(instance=bebida,prefix='form2')
    return render(request, 'cardapio/bebida/edit.html', {'form':form,'form2':form2,'bebida':bebida})  

def cardapioBebidaDestroy(request, id):  
    bebida = Produto.objects.get(id=id)  
    bebida.delete()  
    return redirect("/cardapio/bebida")


