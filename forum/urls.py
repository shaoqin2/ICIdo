from django.conf.urls import url, include
from forum import views

urlpatterns = [
    url(r'^$', views.forum_home, name='ForumHome'),
]
