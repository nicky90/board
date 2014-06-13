from django.core.context_processors import csrf
from django.shortcuts import render, render_to_response
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.http import HttpResponseRedirect

from machines.models import Machine
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    machine_list = Machine.objects.all()
    user = request.session.get('user', '')
    return render(request, 'machines/index.html', {'user': user, 'machine_list': machine_list,})

def profile(request, user):
    pass

def release(request, machine):
    machine = Machine.objects.get(hostname=machine)
    user = request.session.get('user', '')
    user_list = User.objects.all()
    return render_to_response('machines/release.html', {'machine': machine, 'user_list': user_list,})

def applyfor(request, machine):
    pass

def login_view(request):
    return render(request, 'machines/login.html')

def login(request):
    c = {}
    c.update(csrf(request))
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        login(request, user)
        machine_list = Machine.objects.all()
        c.update({'user': user, 'machine_list': machine_list,})
        return render_to_response("machines/index.html", c)
    else:
        return render_to_response("/accounts/login/")

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/machines/", {'user': None,})

def register(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            c.update({'user': '',})
            return render_to_response("machines/index.html", c)
    else:
        form = UserCreationForm()
        c.update({'form': form,})
    return render_to_response("machines/register.html", c)
