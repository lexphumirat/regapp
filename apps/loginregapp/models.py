# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import messages

class UserManger(models.Manager):
    def validate(self,request, post_data):
        if len(post_data['first_name']) < 3 or len(post_data['last_name']) < 3 or len(post_data['email']) < 1:
            messages.error(request, 'You need more than three letters')
        if len(self.filter(email=request.POST['email'])) > 0:
            messages.error(request, 'email needs to be unique')
        if request.POST['password'] != request.POST['confirmpw']:
            messages.error(request, 'your password must match')
        else:
         newuser = User.objects.create(
         first_name = request.POST['first_name'],
         last_name = request.POST['last_name'],
         email = request.POST['email'],
         password = request.POST['password'],
         confirmpw = request.POST['confirmpw']
        )
        print 'hello man'


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    confirmpw = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = UserManger()

    def __str__(self):
        return self.first_name + " " + self.last_name

# Create your models here.
