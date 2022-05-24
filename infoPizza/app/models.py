from django.db import models

class Produto(models.Model):   
    nome = models.CharField(max_length=100,unique=True)  
    desc = models.CharField(max_length=250)
    cat = models.IntegerField()     
    class Meta:  
        db_table = "produto"  

class Pizza(models.Model):
    produto = models.ForeignKey(Produto,on_delete=models.CASCADE,related_name='pizza')
    tamanho = models.CharField(max_length=2,choices=[("B","B"),("M","M"),("G","G"),("GG","GG")])
    preco = models.DecimalField(max_digits=4,decimal_places=2)
    class Meta:
        db_table = "pizza"

class Bebida(models.Model):
    produto = models.ForeignKey(Produto,on_delete=models.CASCADE,related_name='bebida')
    tamanho = models.CharField(max_length=6,choices=[("350ml","350ml"),("600ml","600ml"),("1000ml","1000ml"),("1500ml","1500ml"),("2000ml","2000ml")])
    preco = models.DecimalField(max_digits=4,decimal_places=2)
    quant = models.IntegerField()
    class Meta:
        db_table = "bebida"
