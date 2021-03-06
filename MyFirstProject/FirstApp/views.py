from django.shortcuts import render
from django.http import HttpResponse
from FirstApp.models import Musician, Album

# Create your views here.

def index(request):
    musician_list=Musician.objects.order_by('first_name')
    diction={'musician':musician_list}
    return render(request,'FirstApp/index.html',context=diction)
