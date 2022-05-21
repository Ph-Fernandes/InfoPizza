from telnetlib import theNULL
from django.db import models

class Pizza(models.Model):   
    nome = models.CharField(max_length=100)  
    desc = models.CharField(max_length=250)     
    class Meta:  
        db_table = "pizza"  

class PizzaInfo(models.Model):
    pizza = models.ForeignKey(Pizza,on_delete=models.CASCADE,related_name='infos')
    tamanho = models.CharField(max_length=2,choices=[("B","B"),("M","M"),("G","G"),("GG","GG")])
    preco = models.DecimalField(max_digits=4,decimal_places=2)
    class Meta:
        db_table = "pizzaInfo"

class Bebida(models.Model):   
    nome = models.CharField(max_length=100)  
    desc = models.CharField(max_length=250)     
    class Meta:  
        db_table = "bebida"  

class BebidaInfo(models.Model):
    bebida = models.ForeignKey(Bebida,on_delete=models.CASCADE,related_name='infos')
    tamanho = models.CharField(max_length=6,choices=[("350ml","350ml"),("600ml","600ml"),("1500ml","1500ml"),("2000ml","2000ml")])
    preco = models.DecimalField(max_digits=4,decimal_places=2)
    class Meta:
        db_table = "bebidaInfo"