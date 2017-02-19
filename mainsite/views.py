from django.shortcuts import render
from django.contrib.auth import authenticate, login as LOGIN, logout as LOGOUT
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from mainsite import forms
from .models import *


def home(request):
    dict = {}
    result = Category.objects.all()[:3]
    dict['result'] = result
    try:
        username = request.user
        donor = Donor.objects.get(username=username)
        dict['logged_in'] = True
        dict['catagory_data'] = donor.getDonation()
    except Donor.DoesNotExist:
        dict['logged_in'] = False

    return render(request, 'HomePage.html', dict)

def user_profile(request):
    pass

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
    return render(request,"UserLogin.html",{"form":form,"error":error})

def signup(request):
    return HttpResponse('<h1>Sign up </h1>')
