from django.db import models

# Create your models here.

class Company(models.Model):
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=100)
    type=models.CharField(max_length=100,choices=(('IT',"IT"),('NON IT','NON IT')))
    