from django.db import models

class Item(models.Model):   
    cat = models.SmallIntegerField() 
    nome = models.CharField(max_length=100)  
    desc = models.CharField(max_length=250)     
    class Meta:  
        db_table = "item"  

class ItemInfo(models.Model):
    item = models.ForeignKey(Item,on_delete=models.CASCADE,related_name='infos')
    tamanho = models.CharField(max_length=2,choices=[("B","B"),("M","M"),("G","G"),("GG","GG")])
    preco = models.DecimalField(max_digits=4,decimal_places=2)
    class Meta:
        db_table = "iteminfo"

class ClienteEndereco(models.Model):
    logradouro = models.CharField(max_length=100)
    numero = models.IntegerField(max_length=10)
    complemento = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    cep = models.IntegerField(max_length=8)
    pdr = models.CharField(max_length=300) 

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=100)
    cpf = models.IntegerField(max_length=11)
    endereco = models.OneToOneField(ClienteEndereco,on_delete=models.CASCADE)
    class Meta:
        db_table = "cliente"

class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    itens = models.ManyToManyField(Item)
    status = models.CharField(max_length=50,null=True)       
    preco =  models.DecimalField(max_digits=4,decimal_places=2,null=True) 
    metodo_pag = models.CharField(max_length=50,null=True)
    class Meta:
        db_table = "pedido"


class Mesa(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.BooleanField(default=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE,null=True)
    class Meta:
        db_table = "mesa"