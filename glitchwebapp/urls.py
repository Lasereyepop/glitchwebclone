from django.urls import path
#now import the views.py file into this code
from . import views

urlpatterns=[
    path('', views.index, name="index"),
    path('projects/', views.projects, name='projects'),
    path('join/', views.join, name='join'),
    path('about/', views.about, name='about')
]