from django.db import models

class Book(models.Model):
    book_name=models.CharField(max_length=50)
    author_name=models.CharField(max_length=50)
    book_desc=models.TextField()
    book_cover=models.ImageField(upload_to='book_images/',blank=True,null=True)
    book_id=models.IntegerField(default=-1)
    def __str__(self) -> str:
        return self.book_name + " | Author : " + self.author_name
    
# Create your models here.
