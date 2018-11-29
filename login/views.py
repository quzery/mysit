from django.shortcuts import render,redirect,reverse
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from login.models import User_data
from django import forms

class User_dataform(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)

def auth_login(request):
    if request.POST:
        fm = User_dataform(request.POST)
        if fm.is_valid():
            username = fm.cleaned_data['username']
            password = fm.cleaned_data['password']
            #user = User_data.objects.filter(username = username, password = password)
            user = authenticate(username=username, password=password)
            if user is not None:
                #return render(request, 'home.html', {'username': username})
                login(request, user)
                return redirect('/login/home/')
    fm = User_dataform()
    context = {}
    context.update(csrf(request))
    context = {
        'fm': fm,
    }
    print('hello')
    return render(request, 'login.html',context)

@login_required
def home(request):
    context = {'username':request.user.username,
               }
    return render(request, 'home.html',context)
