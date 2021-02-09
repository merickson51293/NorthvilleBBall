from django.urls import path
from . import views

urlpatterns=[
    path('', views.index),
    path('homepage', views.homepage),
    path('whomepage', views.whomepage),
    path('mschedule', views.mschedule),
    path('wschedule', views.wschedule),
    
]