from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter


# Create your models here.
class Snippet(models.Model):
    id=models.AutoField(primary_key=True)
    created=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=100)
    code=models.TextField()
    language=models.CharField(max_length=100)
    style=models.CharField(max_length=100)
    linenos=models.BooleanField(default=False)
    
    
    class Meta:
        db_table="snippet"
        ordering=['created']
        
    def __str__(self):
        return str(self.title)
    
 
    