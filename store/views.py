from django.contrib.auth.models import User
from pyexpat.errors import messages

from django.contrib import auth
from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def home(request):
    return render(request,'home.html')


def login(request):
    if request.method == 'POST':
        uname=request.POST['username']
        pwd=request.POST['password']
        user=auth.authenticate(username=uname,password=pwd)

        if user is not None:
            auth.login(request,user)
            return redirect('newpage')
        else:
            messages.info(request,"wrong credentials")
            return redirect('login')
    return render(request,'login.html')


def registration(request):
    if request.method == 'POST':
        uname=request.POST['username']
        pwd=request.POST['password']
        cpwd=request.POST['password1']
        if pwd==cpwd:

                return render(request,'login.html')
        else:
            return redirect('register')
    return render(request,'register.html')


def details(request):
    departments = department.objects.all()

    if request.method == 'POST':
        selected_department_id = request.POST.get('department')
        selected_department = department.objects.get(id=selected_department_id)
        Courses = courses.objects.filter(department=selected_department)
        return render(request, 'details.html',
                      {'departments': departments, 'selected_department': selected_department, 'courses': Courses})

    return render(request, 'details.html', {'departments': departments})

def newpage(request):
    return render(request,'newpage.html')




