from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login as LOGIN, logout as LOGOUT
from django.contrib.auth.decorators import login_required

from forum.models import Event


# Create your views here.
@login_required(login_url='/login/')
def display_category_events(request, param):
    pass


def forum_home(request):
    d = {}
    results = Event.objects.all()
    d['events'] = results
    print(results)
    return render(request, 'Forum.html', d)
