from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from account.models import *
from django.db.models import Q


@login_required(login_url='/login/')
def dash(request):
    prof = UserProfile.objects.get(user=request.user)
    materia = MateriaDadas.objects.filter(user=UserProfile.objects.get(user=request.user))
    ctx={'uprofile':prof,'materias':materia}
    return render_to_response('dash.html', ctx,context_instance=RequestContext(request))


@login_required(login_url='/login/')
def history(request):
    prof=UserProfile.objects.get(user=request.user)
    m=Carrera.objects.get(id=prof.carrera.id).materias.all()
    ma=MateriaDadas.objects.filter(user=prof)
    materiasADar=m.filter( (Q(prerequsito__in=ma) | Q(prerequsito=None) )& Q(creditoRequsito__lte=prof.get_credito_apobado())).exclude(id__in=ma.values_list('materia',flat=True))


    ctx={'uprofile':prof,'materias':materiasADar}
    return render_to_response('history.html', ctx,context_instance=RequestContext(request))