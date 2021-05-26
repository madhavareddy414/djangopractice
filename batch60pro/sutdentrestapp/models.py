from django.db import models

# Create your models here.
class Student(models.Model):
    sno = models.IntegerField()
    sname = models.CharField(max_length=20)
    semail = models.CharField(max_length=40)
    sage = models.IntegerField()
    def __str__(self):
        return self.sname
