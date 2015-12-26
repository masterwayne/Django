from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class signup(models.Model):
	username=models.CharField(max_length=50,null=False)
	password
    GENDER_CHOICES = (('M', 'Male'),('F', 'Female'),)
    profile_pic = models.ImageField(upload_to = 'profile_pics/', blank = True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=GENDER_CHOICES[0][0])
    dob = models.DateField(blank=True, null=True)
    phone = PhoneNumberField(unique = True, null=True, blank=True, help_text=('Only Indian'))
    street_address = models.CharField(max_length = 100, null=True, blank=True)
    pincode = models.CharField(max_length=8, default="0000000")