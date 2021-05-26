import uuid

from django.contrib.auth.models import User
from django.utils import timezone

from django.db import models
#pip install django-phonenumber-field,# pip install phonenumbers# in installed 'phonenumber_field'
from django.utils.text import slugify
from phonenumber_field.modelfields import PhoneNumber, PhoneNumberField


class Student(models.Model):
    sname = models.CharField(max_length=125)
    semail = models.EmailField()
    smob = PhoneNumberField()
    sadd = models.CharField(max_length=125)


    def __repr__(self):
        return self.sname
my_choices = (('one','number one'),('two','number two'))

class TestMode(models.Model):
     boolean = models.BooleanField(default=True,verbose_name='this is boolean field')
     char = models.CharField(verbose_name='New name',max_length=220,unique=True,help_text='added help text')
     date = models.DateTimeField(default=timezone.now)
     decimal = models.DecimalField(max_digits=10,decimal_places=2)
     email = models.EmailField(max_length=125)
     file = models.FileField(upload_to='uploads',blank=True)
     image = models.ImageField(upload_to='uploads',blank=True)
     integer = models.IntegerField()
     positive_integer = models.PositiveIntegerField()
     slug = models.SlugField(blank=True)
     text = models.TextField()
     url = models.URLField(max_length=200)
     uuid1 = models.UUIDField(default=uuid.uuid4)
     uuid2 = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
     updated = models.DateTimeField(auto_now=True)
     created = models.DateTimeField(auto_now_add=True)
     date_and_time = models.DateTimeField()
     choice = models.CharField(max_length=10,choices=my_choices)
     phone_number = PhoneNumberField()
     new_field = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

     def save(self ,*args,**kwargs):
         self.slug = slugify(self.text[:30])
         super(TestMode,self).save(*args,**kwargs)