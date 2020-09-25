from django.db import models

# Create your models here.

class Personal(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(max_length=50)

class Cuidador(Personal):
    horas = models.IntegerField(max_length=5)

class Limpiador(Personal):
    horas = models.IntegerField(max_length=5)

class Sector(models.Model):
    sector = models.CharField(max_length=1)
    limpiadores = models.ForeignKey(Limpiador, on_delete=models.CASCADE)

class Animal(models.Model):
    especie = models.CharField(max_length=50)
    sc_name = models.CharField(max_length=50)
    cuidadores = models.ForeignKey(Cuidador, on_delete=models.CASCADE)
    status_options = [
        ('Saludable', 'Saludable'),
        ('En_Veterinario', 'En_Veterinario'),
    ]
    status = models.CharField(max_length=20, choices=status_options, default='Saludable')