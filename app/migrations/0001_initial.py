# Generated by Django 4.0.4 on 2022-06-05 00:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='Inicio', max_length=100)),
                ('tempo', models.DateTimeField(auto_now_add=True)),
                ('metodoPag', models.CharField(max_length=50, null=True)),
                ('obs', models.CharField(max_length=500, null=True)),
            ],
            options={
                'db_table': 'pedido',
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('desc', models.CharField(max_length=250)),
                ('cat', models.IntegerField()),
            ],
            options={
                'db_table': 'produto',
            },
        ),
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField()),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pedido')),
            ],
            options={
                'db_table': 'mesa',
            },
        ),
        migrations.CreateModel(
            name='ItensPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tamanho', models.CharField(max_length=50)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=4)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pedido')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.produto')),
            ],
            options={
                'db_table': 'itensPedido',
            },
        ),
        migrations.CreateModel(
            name='ProdutoInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tamanho', models.CharField(max_length=6)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=4)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bebida', to='app.produto')),
            ],
            options={
                'db_table': 'produtoInfo',
                'unique_together': {('tamanho', 'produto')},
            },
        ),
    ]