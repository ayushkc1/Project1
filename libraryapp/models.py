from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Book(models.Model):
    book_id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    count=models.IntegerField()
    # borrower=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 
    def __str__(self):
        return self.title + "      Available:   " + str(self.count)
   


class Borrow(models.Model):
    borrow_id = models.IntegerField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_borrowed = models.DateField(auto_now_add=True)
    due_date = models.DateField()   
    
    def days_remaining(self):
        today = timezone.localdate()
        remaining = self.date_borrowed - today
        return 45-remaining.days
  
    # def __str__(self):
    #     return self.book.title + " borrowed by " + self.user.username