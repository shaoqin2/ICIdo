from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    dict = {}
    return render(request, 'HomePage.html', dict)

def login(request):
    return HttpResponse('<h1>Login</h1>')

def logout(request):
    return HttpResponse('<h1>LoOut</h1>')
