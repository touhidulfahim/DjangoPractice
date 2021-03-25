from django.shortcuts import render
from django.http import HttpResponse
from FirstApp.models import Musician, Album
from FirstApp import forms
from django.db.models import Avg
# Create your views here.

def index(request):
    musician_list=Musician.objects.order_by('first_name')
    diction={'title':"Home Page",'musician_list':musician_list}
    return render(request,'FirstApp/index.html',context=diction)

def album_list(request, artist_id):
    artist_info=Musician.objects.get(pk=artist_id)
    album_list=Album.objects.filter(artist=artist_id).order_by('name','release_date')
    artist_avg=Album.objects.filter(artist=artist_id).aggregate(Avg('num_stars'))
    diction={'title':"List of Albums",'artist':artist_info,'album_list':album_list, 'AvgRating': artist_avg}
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


def edit_artist(request, artist_id):
    artist_info=Musician.objects.get(pk=artist_id)
    form=forms.MusicianForm(instance=artist_info)
    if request.method=='POST':
        form=forms.MusicianForm(request.POST, instance=artist_info)
        if form.is_valid():
            form.save(commit=True)
            return album_list(request, artist_id)
    diction={'title':"Edit Musician", 'edit_musician_form': form}
    return render(request,'FirstApp/editartist.html', context=diction)


def album_form(request):
    form=forms.AlbumForm()

    if request.method=='POST':
        form=forms.AlbumForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    diction={'title':"Add Album", 'album_form':form}
    return render(request,'FirstApp/album.html', context=diction)

def edit_album(request, album_id):
    album_info=Album.objects.get(pk=album_id)
    form=forms.AlbumForm(instance=album_info)
    diction = {}
    if request.method=='POST':
        form=forms.AlbumForm(request.POST,instance=album_info)
        if form.is_valid():
            form.save(commit=True)
            diction.update({'success_text':'Successfully Updated!'})

    diction.update({'edit_album_form':form})
    diction.update({'album_id':album_id})
    return render(request,'FirstApp/editalbum.html', context=diction)
