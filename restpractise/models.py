from django.db import models

# Create your models here.

class Company(models.Model):
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=100)
    type=models.CharField(max_length=100,choices=(('IT',"IT"),('NON IT','NON IT')))
    def __str__(self):
        return self.name
    

class Employee(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    
    