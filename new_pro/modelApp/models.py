from django.db import models

class Employee(models.Model):
    eno = models.IntegerField()
    ename= models.CharField(max_length=30)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=30)

    def __repr__(self):
        return self.ename

class Empsalary(models.Model):
    eno = models.IntegerField(primary_key=True)
    ename= models.CharField(max_length=30)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=30)

    class Meta:
        db_table = "empsalary"

    def __repr__(self):
        return self.ename
