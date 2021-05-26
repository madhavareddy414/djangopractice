import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','enrolmentCB.settings')
import django
django.setup()
from register.models import Student
from faker import Faker

fakegen = Faker()

def generate(N=10):
    for i in range(N):
        name = fakegen.name()
        email = fakegen.email()
        mob = fakegen.phone_number()
        sch = fakegen.address()
        add = fakegen.address()
        student = Student.objects.get_or_create(sname=name,semail=email,smob=mob,ssch=sch,sadd=add)

if __name__ =='__main__':
    print('generating')
    generate(500)
    print('population complete')