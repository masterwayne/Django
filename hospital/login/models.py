from django.db import models

# Create your models here.

class login(models.Model)
      user_id = models.AutoField()
      username = models.CharField(max_length = 100)
      password = models.TextField()
      category = models.TextField()
