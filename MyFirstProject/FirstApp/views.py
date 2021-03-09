from django.shortcuts import render
from django.http import HttpResponse
from FirstApp.models import Musician, Album
from FirstApp import forms
# Create your views here.

def index(request):
    musician_list=Musician.objects.order_by('first_name')
    diction={'text_1':'This a list of Musicians','musician':musician_list}
    return render(request,'FirstApp/index.html',context=diction)

def form(request):
    new_form=forms.MusicianForm()
    if request.method=='POST':
        new_form=forms.MusicianForm(request.POST)
        if new_form.is_valid():
            new_form.save(commit=True)
            return index(request)



    diction={'test_form': new_form,'heading_1':'Add new Musician'}
    return render (request, 'FirstApp/form.html', context=diction)
