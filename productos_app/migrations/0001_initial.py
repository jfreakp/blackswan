# Generated by Django 4.0.2 on 2022-03-14 01:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], default='M', max_length=1)),
                ('talla', models.CharField(max_length=20)),
                ('precio_normal', models.PositiveIntegerField()),
                ('precio_oferta', models.PositiveIntegerField()),
                ('stock', models.PositiveIntegerField(default=1)),
                ('oferta', models.BooleanField(default=False)),
                ('imagen', models.ImageField(upload_to='images/p/')),
                ('vigente', models.BooleanField(default=True)),
                ('categoria', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='productos_app.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.IntegerField(default=0)),
                ('nombre', models.CharField(default=' ', max_length=100)),
                ('cantidad', models.PositiveIntegerField(default=0)),
                ('imagen', models.ImageField(blank=True, upload_to='images/')),
                ('precio', models.PositiveIntegerField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('activo', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
