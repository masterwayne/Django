from django.db import models

class signup(models.Model):
	username=models.CharField(max_length=50,null=False)
	password=models.CharField(max_length=50,null=False)
	GENDER_CHOICES = (('M', 'Male'),('F', 'Female'),)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=GENDER_CHOICES[0][0])
	dob = models.DateField(blank=True, null=True)
	street_address = models.CharField(max_length = 100, null=True, blank=True)
	pincode = models.CharField(max_length=8, default="0000000")

   

