from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    book_id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    count=models.IntegerField()
    def __str__(self):
        return self.title,self.count
   


class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_borrowed = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    
