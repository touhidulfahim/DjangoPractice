from django.conf.urls import url
from django.urls import path
from FirstApp import views

app_name="FirstApp"


urlpatterns=[
    path('', views.index, name='index'),
    path('album/', views.album_form, name='Album'),
    path('musician/', views.musician_form, name='Musician'),
    path('albumlist/<int:artist_id>/', views.album_list, name='albumlist'),
    path('editartist/<int:artist_id>/', views.edit_artist, name='editartist'),
    path('editalbum/<int:album_id>/', views.edit_album, name='editalbum')
]
