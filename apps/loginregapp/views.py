from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import User
from django.contrib import auth




def index(request):
    #to use context in index route
    context = {
        'listallusers': User.objects.all()
    }
    return render(request , 'loginregapp/index.html', context)

def showuser(request):
    print 'show me'
    users = User.objects.all()
    context = {
        'listallusers': User.objects.all()
    }
    #get or filter
    if not User.objects.filter(email=request.POST['emaillogin']):
        return render(request, '/')
    else:
        return render(request , 'loginregapp/showuser.html', context)

def register(request):
    User.objects.validate(request, request.POST)
    return redirect('/')
