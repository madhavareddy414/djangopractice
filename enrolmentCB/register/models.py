from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField


class Student(models.Model):
    sname = models.CharField(max_length=30)
    semail = models.EmailField(max_length=100)
    smob = models.CharField(max_length=15)
    ssch = models.CharField(max_length=100)
    sadd = models.CharField(blank=True,max_length=100)


    def __str__(self):
        return self.sname


    def get_absolute_url(self):
        return reverse('Student-Registration',args=str(self.id))


class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=30)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=30)

    def __str__(self):
        return self.ename

class EmpSalary(models.Model):
    eno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=30)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=30)

    def __str__(self):
        return self.ename

