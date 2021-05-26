import os

import faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE','studentreg.settings')
import django
django.setup()
from register.models import Student
from faker import Faker

fakegen = Faker()

def populate(N=30):
    for i in range(N):
        name = fakegen.name()
        email = fakegen.email()
        mob = fakegen.phone_number()
        add = fakegen.address()
        student =Student.objects.get_or_create(sname=name,semail = email,sadd=add,smob=mob)

if __name__=='__main__':
    print('populating data please wait...')
    populate(100)
    print('population complete')