from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    carrera = models.OneToOneField('Carrera')

    def __unicode__(self):
        return self.user.email


class Carrera(models.Model):
    id = models.CharField('ID', primary_key=True,max_length=3)
    pensum= models.OneToOneField('Pensum')

class Pensum(models.Model):
    materias=models.ManyToManyField('Materia')


class Materia(models.Model):
    id = models.CharField('ID', primary_key=True,max_length=6)
    nombre = models.CharField(blank=False, null=False,max_length=60)
    credito = models.IntegerField()
    creditoRequsito = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    rate = models.IntegerField()

class Prerequisito(models.Model):
     materia = models.ManyToManyField('Materia')