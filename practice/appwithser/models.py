from django.db import models

class Employee(models.Model):
    eno = models.IntegerField()
    ename= models.CharField(max_length=250)
    esal = models.FloatField()
    edd = models.CharField(max_length=250)

    def __str__(self):
        return self.ename