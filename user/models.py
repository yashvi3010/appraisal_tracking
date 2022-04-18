from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
# class User(models.Model):
#     username = models.CharField(max_length=20)
#     email = models.EmailField(null=True)
#     password = models.CharField(max_length=20)

#     class Meta():
#         db_table = 'user'

class User(AbstractUser):
    is_employee = models.BooleanField(default=True)
    is_hr = models.BooleanField(default=True)

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Hr(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
