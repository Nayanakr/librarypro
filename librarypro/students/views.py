from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse

def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        cp=request.POST['cp']
        fname=request.POST['f']
        lname=request.POST['l']
        e=request.POST['e']
        if(p==cp):
           user=User.objects.create_user(username=u,password=p,first_name=fname,last_name=lname,email=e)
           user.save()
           return redirect('books.home')
        else:
           return HttpResponse("password are not same")

    return render(request,'register.html')
def login(request):
    return render(request,'login.html')
