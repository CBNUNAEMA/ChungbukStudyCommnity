from .views import *
from django.urls import path

app_name = 'board'

urlpatterns = [
    path('', index, name = 'home'),
    path('post/<str:lectName>', lectBoard, name = 'board'),
    path('post/<str:lectName>/newPost/', NewPost, name='NewPost'),
    path('post/<str:lectName>/see/<int:pk>/', Posting, name ='Posting'),
    path('eval/', evalMain, name='eMain'),
    path('eval/lect/<str:lectName>', evalBoard, name='eBoard'),
    path('post/<str:lectName>/tag/<str:tag>/', boardWithTag, name='boardWithTag'),
]
