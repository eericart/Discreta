from django.http import HttpResponse
from account.models import *
# Integramos la serializacion de los objetos
from django.core import serializers



def wsUser_view(request):
    data = serializers.serialize("json",User.objects.all())
    return HttpResponse(data,mimetype='application/json')

def wsProf_view(request):
    data = serializers.serialize("json",Profesor.objects.all())
    return HttpResponse(data,mimetype='application/json')