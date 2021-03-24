from django.shortcuts import render
from django.http import HttpResponse
from FirstApp.models import Musician, Album
from FirstApp import forms
# Create your views here.

def index(request):
    musician_list=Musician.objects.order_by('first_name')
    album_list=Album.objects.all()
    diction={'title':"Home Page",'musician_list':musician_list,'album_list':album_list}
    return render(request,'FirstApp/index.html',context=diction)

def album_list(request):
    diction={'title':"List of Albums"}
    return render(request,'FirstApp/albumlist.html', context=diction)

def musician_form(request):
    form=forms.MusicianForm()

    if request.method=='POST':
        form=forms.MusicianForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    diction={'title':"Add Musician", 'musician_form': form}
    return render(request,'FirstApp/musician.html', context=diction)

def album_form(request):
    form=forms.AlbumForm()

    if request.method=='POST':
        form=forms.AlbumForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    diction={'title':"Add Album", 'album_form':form}
    return render(request,'FirstApp/album.html', context=diction)
