from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=20)
    user = models.OneToOneField(User,on_delete=models.CASCADE,default=1)
    content = models.CharField(max_length=100)
    unique_code = models.CharField(max_length=20)

