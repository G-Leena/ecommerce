from django.shortcuts import render,redirect
from app55 import models as app55_models 
# Create your views here.

def adminhome(request):
    return render(request,'adminhome.html')

def manageuser(request):
    uDetails=app55_models.Registretion.objects.filter(roll="user")
    print(uDetails)
    return render(request,"manageuser.html",{"uDetails":uDetails})

def manageuserstatus(request):
    regid=int(request.GET.get("regid"))
    s=request.GET.get("s")
    if s=="verify":
        app55_models.Registretion.objects.filter(regid=regid).update(status=1)
    elif s=="block":
        app55_models.Registretion.objects.filter(regid=regid).update(status=0)
    else:
        app55_models.Registretion.objects.filter(regid=regid).delete()
    return redirect("/myadmin/manageuser/")

