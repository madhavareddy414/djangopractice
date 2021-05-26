from django.db import models

class Student(models.Model):
    sname = models.CharField(max_length=30)
    sdep = models.CharField(max_length=30)
    srno = models.CharField(max_length=30)
    semail = models.EmailField(max_length=30)
    smob = models.IntegerField(max_length=30 )

    def __str__(self):
        return self.sname


class Faculty(models.Model):
    fname = models.CharField(max_length=30)
    fdep = models.CharField(max_length=30)
    fsal = models.IntegerField(max_length=30)

    def __str__(self):
        return self.fname

class Subjects(models.Model):
    telugu=models.IntegerField()
    hindi = models.IntegerField()
    english = models.IntegerField()
    maths = models.IntegerField()
    science = models.IntegerField()
    social = models.IntegerField(max_length=30)

    def __str__(self):
        return self.sname

