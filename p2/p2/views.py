from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    data={
        "title":"Welcome to Tryst"
    }
    return render(request, "index.html",data)

def contactUs(request):
    data={
        "title":"Contact Us",
        "phone1":'1234567890',
        "phone2":'6666666666',
        "email1":'hohoho123@keshav.du.edu.ac.in'
    }
    return render(request, "contactus.html",data)

def registration(request):
    data={
        "title":"Registration"
    }
    return render(request, "registration.html",data)
