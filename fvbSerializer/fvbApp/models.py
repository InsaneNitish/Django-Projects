from django.db import models
class Student(models.Model):
    rollno=models.IntegerField(primary_key=True)
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)

    def __str__(self):
        return self.fname + " " + self.lname
# Create your models here.
