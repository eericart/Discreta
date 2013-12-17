from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from account.models import User, UserProfile
from account.form import LoginForm, RegistrationForm
from django.contrib.auth import login , logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

#Authenticated
def login_v(request): #Log in View
    msg=''
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        if request.method=="POST":
            form=LoginForm(request.POST)
            if form.is_valid():
                email=form.cleaned_data['email']
                password=form.cleaned_data['password']
                auth_user=authenticate(email=email,password=password)
                if auth_user is not None and auth_user.is_active:
                    login(request,auth_user)
                    return HttpResponseRedirect('/')
                else:
                    msg='Wrong Email and password combination.'
        form=LoginForm()
        ctx={'form':form,'mensaje':msg}
        return render_to_response('login.html',ctx, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def logout_v(request):
	logout(request)
	return HttpResponseRedirect('/')

#Registration
def sign_up(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		if request.method=="POST":
			form=RegistrationForm(request.POST)
			if form.is_valid():
				name=form.cleaned_data['name']
				lastname=form.cleaned_data['lastname']
				email=form.cleaned_data['email']
				password=form.cleaned_data['password']
				birthday=form.cleaned_data['birthday']
				country=form.cleaned_data['country']
				new_u=User.objects.create_user(username= email, email= email, password=password)
				new_u.first_name=name
				new_u.last_name=lastname
				new_u.save()
				UserProfile.objects.create(user=new_u)
				new_p=UserProfile.objects.get(user=new_u)
				new_p.birthday=birthday
				new_p.country=country
				new_p.save()
				new_user = authenticate(email=email,password=password)
				login(request, new_user)
				return HttpResponseRedirect('/' )

		form=RegistrationForm()
		ctx={'form':form,}
		return render_to_response('signup.html',ctx, context_instance=RequestContext(request))
