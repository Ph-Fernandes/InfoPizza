# Generated by Django 4.0.4 on 2022-06-25 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_pedido_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
