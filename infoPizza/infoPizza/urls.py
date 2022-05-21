from django.contrib import admin  
from django.urls import path  
from app import views
urlpatterns = [  
    path('admin/', admin.site.urls),
    path('',views.index),
    path('cardapio/',views.cardapioIndex),
    path('cardapio/pizza/',views.cardapioPizzaIndex),
    path('cardapio/pizza/insert',views.cardapioPizzaInsert),
    path('cardapio/pizza/edit/<int:id>',views.cardapioPizzaUpdate),
    path('cardapio/pizza/delete/<int:id>',views.cardapioPizzaDestroy),
    path('cardapio/bebida/',views.cardapioBebidaIndex), 
    path('cardapio/bebida/insert',views.cardapioBebidaInsert),
    path('cardapio/bebida/edit/<int:id>',views.cardapioBebidaEdit),
    path('cardapio/bebida/update/<int:id>',views.cardapioBebidaUpdate),
    path('cardapio/bebida/delete/<int:id>',views.cardapioBebidaDestroy),
    path('pedidos/',views.pedidosIndex),
    path('pedidos/mesa/order/<int:id>',views.pedidosMesaOrder),
    path('caixa/mesa/insert',views.caixaMesaInsert)
]  