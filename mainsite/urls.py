from django.conf.urls import url, include
from mainsite import views

urlpatterns = [
    url(r'^$', views.home, name='HomePage'),
    url(r'^login/', views.login, name='LoginPage'),
    url(r'^logout/', views.logout, name='LogOut'),
]
