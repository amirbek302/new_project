from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    age = models.PositiveIntegerField(null=True,blank=True)
    work = models.CharField(max_length=100,blank=True)
    hobby = models.JSONField(default=list,blank=True)