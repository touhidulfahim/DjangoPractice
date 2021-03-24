from django.conf.urls import url
from django.urls import path
from FirstApp import views

app_name="FirstApp"


urlpatterns=[
    path('', views.index, name='index'),
    path('album/', views.album_form, name='Album'),
    path('musician/', views.musician_form, name='Musician')

]
