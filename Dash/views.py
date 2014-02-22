from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from account.models import *
from django.db.models import Q


@login_required(login_url='/login/')
def dash(request):
    prof = UserProfile.objects.get(user=request.user)
    materia = MateriaDadas.objects.filter(user=UserProfile.objects.get(user=request.user))
    try:
        period=Periods.objects.filter(Q(user=prof) & Q(num=prof.get_Total_Trimestre))[0].materia.all()
    except:
        period=[]
    ctx={'uprofile':prof,'materias':period}
    return render_to_response('dash.html', ctx,context_instance=RequestContext(request))


@login_required(login_url='/login/')
def program(request):
    user=UserProfile.objects.get(user=request.user)
    materiasADar=Carrera.objects.get(id=user.carrera_id).materias.all().filter(Q(id="ELE") |Q(prerequsito=None) |Q(prerequsito__in=MateriaDadas.objects.filter(user=user).values_list('materia',flat=True))).exclude(Q(id__in=MateriaDadas.objects.filter(user=user).values_list('materia',flat=True)) & ~Q(id__in=Materia.objects.filter(id="ELE"))).exclude(id__in=Materia.objects.filter(creditoRequsito__gt=user.get_credito_apobado()))

    ctx={'uprofile':user,'materias':materiasADar}
    return render_to_response('program.html', ctx,context_instance=RequestContext(request))


@login_required(login_url='/login/')
def history(request):
    prof=UserProfile.objects.get(user=request.user)
    period=Periods.objects.filter(Q(user=prof))


    ctx={'uprofile':prof,'periods':period}
    return render_to_response('history.html', ctx,context_instance=RequestContext(request))

