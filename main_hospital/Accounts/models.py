from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.

class MyUser(models.Model):
	FirstName=models.CharField(max_length=200)
	LastName=models.CharField(max_length=200)
	password=models.CharField(max_length=200)
	username=models.CharField(max_length=200)
	Confirm_Password=models.CharField(max_length=200)
	Email_Id=models.CharField(max_length=200)
 	
	def __unicode__(self):
		return self.title
