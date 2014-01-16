from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    carrera = models.ForeignKey('Carrera')

    def __unicode__(self):
        return self.user.email

    def get_credito_apobado (self):
        ap=0
        materia=MateriaDadas.objects.filter(user=self)
        for m in materia:
            ap += m.materia.credito
        return ap



class Carrera(models.Model):
    id = models.CharField('ID', primary_key=True,max_length=3)
    nombre = models.CharField(max_length=30, blank=False, null=False)
    materias=models.ManyToManyField('Materia')

    def __unicode__(self):
        return u'%s %s' % (self.id, self.nombre)


class Materia(models.Model):
    id = models.CharField('ID', primary_key=True,max_length=6)
    nombre = models.CharField(blank=False, null=False,max_length=60)
    credito = models.IntegerField()
    creditoRequsito = models.IntegerField(default=0)
    importancia = models.IntegerField(default=0)
    profesor = models.ManyToManyField('Profesor')
    prerequsito = models.ManyToManyField('Materia', null=True, blank=True)

    def __unicode__(self):
        return u'%s %s' % (self.id, self.nombre)

class Profesor(models.Model):
    nombre = models.CharField(max_length=30, blank=False, null=False)
    appellido = models.CharField(max_length=30, blank=False, null=False)

    def getFull_name (self):
        return u'%s, %s' % (self.nombre, self.appellido)

    def __unicode__(self):
        return u'%s, %s' % (self.appellido, self.nombre)

class ProfesorRate (models.Model):
    profesor = models.ForeignKey('Profesor')
    user = models.ForeignKey('UserProfile')
    rate = models.IntegerField(default=0)

class MateriaDadas (models.Model):
    materia = models.ForeignKey('Materia')
    user = models.ForeignKey('UserProfile')
    aprobada = models.BooleanField(default=False)