from django.contrib import admin
from testapp.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ['rollno','name','dob','marks','email','phone_number','address']

admin.site.register(Student,StudentAdmin)
