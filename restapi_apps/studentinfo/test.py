import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','studentinfo.settings')
import django
django.setup()

from testapp.models import Student
from random import randint
from faker import Faker

fake = Faker()


def phone_number():
    d=randint(6,9)
    number = str(d)
    for i in range(9):
        number= number+str(randint(0,9))
    return int(number)


def populate(n):
    print('populating data....')
    for each in range(n):

        frollno=fake.random_int(min=1,max=999)
        fname= fake.name()
        fdob= fake.date_time()
        fmarks = fake.random_int(min=1,max=100)
        femail = fake.email()
        fphonenumber= phone_number()
        faddress= fake.address()

        studen_recored= Student.objects.create(rollno=frollno,name=fname,dob=fdob,marks=fmarks,email=femail,phone_number=fphonenumber,address=faddress)
    print('population completed')
populate(50)