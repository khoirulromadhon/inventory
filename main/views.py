from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def index(response):
    return render(response, "main/home.html")

def lihat(response):
    return render(response, "main/lihat.html")

def about(response):
    return render(response, "main/about.html")