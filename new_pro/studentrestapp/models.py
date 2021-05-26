from django.db import models

class Student(models.Model):
    sno = models.IntegerField()
    sname = models.CharField(max_length=20)
    smail = models.CharField(max_length=40)
    sage = models.IntegerField()
    def __str__(self):
        return self.sname