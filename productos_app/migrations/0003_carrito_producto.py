# Generated by Django 4.0.2 on 2022-03-08 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos_app', '0002_carrito_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito',
            name='producto',
            field=models.IntegerField(default=0),
        ),
    ]
