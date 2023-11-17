
from django.urls import path 

from . import views

urlpatterns = [
    path('', views.adminhome),
    path('manageuser/', views.manageuser),
    path('manageuserstatus/',views.manageuserstatus),
    
    
     
    
    
]

