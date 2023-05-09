from django.db import models

# Create your models here.
class Book(models.Model):
    Book_id=models.IntegerField(primary_key=True)
    Book_name=models.CharField(max_length=100)
    Author=models.CharField(max_length=100)
    Book_Issue_Date=models.DateField()
    