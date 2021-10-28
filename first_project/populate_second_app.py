import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

from second_app.models import User
from faker import Faker

fakegen =Faker()

def populate(N=5):
    for entry in range(N):
        fake_firstName = fakegen.first_name()
        fake_lastName = fakegen.last_name() 
        fake_email = fakegen.email()
        user  = User.objects.get_or_create(first_name=fake_firstName, last_name=fake_lastName, email=fake_email)[0]

if __name__=='__main__':
    print("populating script!")
    populate(20)
    print("populating completed")
