from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from Home.form import Contact
from django.core.mail import send_mail, BadHeaderError
from account.models import Profesor
from django.core.paginator import Paginator,EmptyPage,InvalidPage


def home(request):
    return render_to_response('index.html', context_instance=RequestContext(request))


def about(request):
    mensage = "Mensage de about"
    ctx = {'msg': mensage}
    return render_to_response('about.html', ctx, context_instance=RequestContext(request))



def contacto(request):
    enviado=False
    if request.method == "POST":
        formulario = Contact(request.POST)
        if formulario.is_valid():
            enviado = True
            name = formulario.cleaned_data['name']
            email = formulario.cleaned_data['Email']
            asunto = formulario.cleaned_data['asunto']
            texto = formulario.cleaned_data['Texto']
            cc_myself = formulario.cleaned_data['cc_myself']

            #Correo
            recipients = ['ernest2193@gmail.com']
            if cc_myself:
                recipients.append(email)
            msg = "Hi there, "+name+"\n\nThanks for getting in touch.\nHere's what we got from you:\n" + texto +"\n\nX Customer Service Team"
            try:
                send_mail(asunto, msg, email, recipients)
            except BadHeaderError:
            		return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/contact/thanks/')
    else:
        formulario = Contact()
    ctx = {'form': formulario,'enviado': enviado}
    return render_to_response('contacto.html', ctx, context_instance=RequestContext(request))

def thankyou(request):
    return render_to_response('thanks.html')

def profesores_v(request,pagina):
    profesorList = Profesor.objects.all();
    paginator = Paginator(profesorList,10);
    try:
        page = int(pagina)
    except:
        page = 1
    try:
        profesores = paginator.page(page)
    except (EmptyPage,InvalidPage):
        profesores = paginator.page(paginator.num_pages)
    ctx = {'profesores':profesores}
    return render_to_response('Profesores.html',ctx,context_instance=RequestContext(request))
def singleProfe_v(request):
    pass


