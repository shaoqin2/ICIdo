from django.conf.urls import url, include
from mainsite import views

urlpatterns = [
    url(r'^$', views.home, name='HomePage'),
    url(r'^Category/<>', views.home, name='Categories')
]
