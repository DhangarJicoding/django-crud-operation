from django.shortcuts import render,redirect
from django.http import HttpResponse,request
from .models import *
# Create your views here.
def home(request):
    return render(request,'ragister.html')


def insert(request):
    first=request.POST['firstname']
    last=request.POST['lname']
    Email=request.POST['email']
    Number=request.POST['number']
    newuser=Student.objects.create(fname=first,lname=last,email=Email,number=Number)
    return redirect('showpage')

def showpage(request):
    alldata=Student.objects.all()
    return render(request,'show.html',{'key1':alldata})

def editpage(request,pk):
    get_data=Student.objects.get(id=pk)
    return render(request,'edit.html',{'key2':get_data})

def update(request,pk):
    uname=Student.objects.get(id=pk)
    uname.fname=request.POST['firstname']
    uname.lname=request.POST['lname']
    uname.email=request.POST['email']
    uname.number=request.POST['number']
    uname.save()
    return redirect(showpage)
def deletedata(request,pk):
    data=Student.objects.get(id=pk)
    data.delete()
    return redirect(showpage)