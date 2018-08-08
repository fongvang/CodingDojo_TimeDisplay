from django.shortcuts import render, HttpResponse, redirect
from time import localtime, strftime

def index(request):
    context = {
        "date": strftime("%b %d, %Y", localtime()),
        "time": strftime("%#I:%M %p", localtime())
    }
    
    return render(request,'first_app/index.html', context)
    