from django.shortcuts import render
from django.http import HttpResponse
from FirstApp.models import Musician, Album
from FirstApp import forms
# Create your views here.

def index(request):
    diction={'title':"Home Page"}
    return render(request,'',context=diction)

def album_list(request):
    diction={'title':"List of Albums"}
    return render(request,'', context=diction)

def musician_form(request):
    diction={'title':"Add Musician"}
    return render(request,'', context=diction)

def album_form(request):
    diction={'title':"Add Album"}
    return render(request,'', context=diction)
