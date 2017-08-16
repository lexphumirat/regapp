from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import User



def index(request):
    return render(request , 'loginregapp/index.html')

def showuser(request):
    context = {
        'listallusers': User.objects.all()
    }
    return redirect('/' , context)

def register(request):
    User.objects.validate(request, request.POST)
    return redirect('/')
