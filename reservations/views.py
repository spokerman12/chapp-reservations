from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def dumb(request, data = None):
    return HttpResponse("Hellodumb %s." % data)
