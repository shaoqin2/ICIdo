from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login as LOGIN, logout as LOGOUT
from django.contrib.auth.decorators import login_required

from forum.models import Event


# Create your views here.
@login_required(login_url='/login/')
def display_category_events(request, param):
    categories = #intercept part of the url to use for
    #^'/<regular expression>'



# redirect to the homepage
def home(request):
    dict = {}
    result = 'mainsite.Category'.objects.all()[:3]
    dict['result'] = result
    return render(request, 'HomePage.html', dict)

