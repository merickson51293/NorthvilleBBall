from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    return render(request, "index.html")

def homepage(request):
    return render(request, "home.html")

def whomepage(request):
    return render(request, "whome.html")

def mschedule(request):
    return render(request, "mschedule.html")

def wschedule(request):
    return render(request, "wschedule.html")