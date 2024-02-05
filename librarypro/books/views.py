from django.shortcuts import render
from django.db.models import Q
from books.forms import bookform
from books.models import Book
#from django.http import HttpResponse
def home(request):
    return render(request,'home.html')
def add(request):
    if(request.method=="POST"):  #afrer submition of form
        t=request.POST['t']
        a=request.POST['a']
        p=request.POST['p']
        f=request.FILES['f']
        i=request.FILES['i']
        b=Book.objects.create(title=t,author=a,price=p,pdf=f,cover=i)
        b.save()
        return view(request)
    return render(request,'addbooks.html')
def detail(request,p):
    b=Book.objects.get(id=p)
    print(p)
    return render(request,'bookdetail.html',{'b':b})

def edit(request,p):
    b = Book.objects.get(id=p)
    if (request.method == "POST"):  # after submission
        form = bookform(request.POST,request.FILES,instance=b)  # creates form object initialized with values inside request.POST
        if form.is_valid():
            form.save()  # saves form object in db model
            return view(request)
    form=bookform(instance=b)
    return render(request,'edit.html',{'form':form})

def search(request):
    b= None
    q= ""
    if (request.method == "POST"):
        q = request.POST['q']
        b = Book.objects.filter(Q(titile__icontains=q)| Q(author__icontains=q))
    return render(request,'search.html',{'q':q,'b':b})

def delete(request,p):
    b=Book.objects.get(id=p)
    b.delete()
    return view(request)
def view(request):
    k=Book.objects.all()
    return render(request,'viewbooks.html',{'b':k})
def add1(request):
    if(request.method=="POST"):  #after submission
        form=bookform(request.POST)  #creates form object initialized with values inside request.POST
        if form.is_valid():
            form.save()    #saves form object in db model
            return view(request)

    form=bookform()        #creates empty form object
    return render(request,'addbook1.html',{'form':form})
def fact(request):
    if(request.methode=="POST"):
        num=request.POST['n']
       # factorial--1*2*3*--num
        f=1
        for i in range(1,num+1):
            f=f*i
        return render(request,'fact.html',{'fact':f})

    return render(request,'fact.html')