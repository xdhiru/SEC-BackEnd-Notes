from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    data={
        "title1":"Welcome to Tryst"
    }
    return render(request, "index.html",data)

def contactUs(request):
    return render(request, "index.html")
