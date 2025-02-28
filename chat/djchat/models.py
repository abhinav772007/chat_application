from django.db import models
from datetime import datetime

# Create your models here.
class room(models.Model):
    name = models.CharField(max_length=1000)
   

class message(models.Model):
    value = models.CharField(max_length=1000000)
    date= models.DateTimeField(default=datetime.now,blank=True)
    user = models.CharField(max_length=1000)
    room = models.CharField(max_length=1000)  

class signup(models.Model):
    username = models.CharField(max_length=1000)
    password = models.CharField(max_length=1000)  


class Feedback(models.Model):
    Uname = models.CharField(max_length=1000,default="None")
    rattings = models.CharField(max_length=1000)
    comment = models.CharField(max_length=1000)       

