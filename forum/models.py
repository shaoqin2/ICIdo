from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    brief = models.CharField(max_length=500)
    link = models.URLField(blank=True)
    # not to display
    categories = models.ManyToManyField('mainsite.Category')

    # internal use only
    haveToHost = models.BooleanField()

    # if haveToHost, need these fields
    affiliation = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=5000, blank=True)

