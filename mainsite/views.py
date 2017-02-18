from django.shortcuts import render
from django.contrib.auth import authenticate, login as LOGIN, logout as LOGOUT
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from mainsite import forms


def home(request):
    dict = {}
    return render(request, 'HomePage.html', dict)

def logout(request):
    return HttpResponse('<h1>LoOut</h1>')

def login(request):
    form = forms.LoginForm()
    error = ""
    if request.method=='POST':
            form = forms.LoginForm(request.POST)
            if form.is_valid():
                    user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
                    if user is not None:
                            LOGIN(request,user)
                            return HttpResponseRedirect('/')
                    else:
                            error = "Invalid Password or Username"
            else:
                    error = "Please input valid credentials"
    return render(request,"Login.html",{"form":form,"error":error})
