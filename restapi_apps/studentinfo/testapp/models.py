from django.db import models

class Student(models.Model):
    rollno= models.IntegerField()
    name = models.CharField(max_length=64)
    dob = models.IntegerField()
    marks = models.IntegerField()
    email = models.EmailField()
    phone_number= models.IntegerField()
    address = models.CharField(max_length=64)