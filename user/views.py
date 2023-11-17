from django.shortcuts import render
from django.conf import settings
# from . import views
# Create your views here.

def userhome(request):
    return render(request,"userhome.html")