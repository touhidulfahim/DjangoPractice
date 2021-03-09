from django.shortcuts import render
from django.http import HttpResponse
from FirstApp.models import Musician, Album
from FirstApp import forms
# Create your views here.

def index(request):
    musician_list=Musician.objects.order_by('first_name')
    diction={'musician':musician_list}
    return render(request,'FirstApp/index.html',context=diction)

def form(request):
    new_forms=forms.user_form()
    diction={'userForm':new_forms}
    if request.method=='POST':
        new_forms=forms.user_form(request.POST)
        if new_forms.is_valid():
            user_name=new_forms.cleaned_data['user_name']
            user_email=new_forms.cleaned_data['user_email']
            user_dob=new_forms.cleaned_data['user_dob']

            diction.update({'user_name':user_name})
            diction.update({'user_dob':user_dob})
            diction.update({'user_email':user_email})
            diction.update({'form_submited':"Yes"})


    return render (request, 'FirstApp/form.html', context=diction)
