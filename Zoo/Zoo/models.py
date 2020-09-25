from django.db import models

# Create your models here.

class Personal(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

    class Meta:
        verbose_name = ('Personal')
        verbose_name_plural = ('Personales')


class Cuidador(Personal):
    horas = models.IntegerField()

    class Meta:
        verbose_name = ('Cuidador')
        verbose_name_plural = ('Cuidadores')

class Limpiador(Personal):
    horas = models.IntegerField()

    class Meta:
        verbose_name = ('Limpiador')
        verbose_name_plural = ('Limpiadores')

class Sector(models.Model):
    sector = models.CharField(max_length=1)
    limpiadores = models.ForeignKey(Limpiador, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ('Sector')
        verbose_name_plural = ('Sectores')

class Animal(models.Model):
    especie = models.CharField(max_length=50)
    sc_name = models.CharField(max_length=50)
    cuidadores = models.ForeignKey(Cuidador, on_delete=models.CASCADE)
    status_options = [
        ('Saludable', 'Saludable'),
        ('En_Veterinario', 'En_Veterinario'),
    ]
    status = models.CharField(max_length=20, choices=status_options, default='Saludable')
    foto = models.ImageField(max_length=100,upload_to='Zoo/',default='Zoo/default.png',blank=True)

    class Meta:
        verbose_name = ('Animal')
        verbose_name_plural = ('Animales')