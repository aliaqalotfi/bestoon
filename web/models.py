from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class Expense(models.Model):
#
#     text=models.CharField(_( max_length=250)
#
#     date =models.DateTimeField()
#     amount =models.BigIntegerField()
#     user= models.ForeignKey(User, on_delete=models.CASCADE)
class Expense(models.Model):
    text=models.CharField( max_length=250)
    time=models.DateTimeField()
    amount =models.BigIntegerField()
    user= models.ForeignKey(User, on_delete=models.CASCADE)



class Income(models.Model):
    text=models.CharField( max_length=250)
    time=models.DateTimeField()
    amount =models.BigIntegerField()
    user= models.ForeignKey(User, on_delete=models.CASCADE)
