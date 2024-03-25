# create_dummy_data.py

import os
import django
import random
import string

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cns.settings')
django.setup()

from user.models import UserType, Address, User
from user.models import *

def create_dummy_data():
    # Create dummy UserType instances
    user_types = ['customer', 'provider']
    for user_type in user_types:
        UserType.objects.create(user_type=user_type)

    # Create dummy Address instances
    for _ in range(10):
        Address.objects.create(
            add1=f'Address line 1 {_+1}',
            add2=f'Address line 2 {_+1}',
            city='City',
            address_type=random.choice(['user', 'serviceprovider', 'servicebooking']),
            provision='Provision',
            country='Country',
            postal_code='12345',
            latitude='123.456',
            longitude='456.789'
        )

    # Create dummy User instances
    for _ in range(10):
        first_name = ''.join(random.choices(string.ascii_letters, k=8))
        last_name = ''.join(random.choices(string.ascii_letters, k=8))
        email = f'{first_name}.{last_name}@example.com'
        phone_number = ''.join(random.choices(string.digits, k=10))
        avatar = 'path/to/avatar.jpg'  # Adjust as needed
        bio = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
        gender = random.choice(['male', 'female', 'other'])
        currency_code = random.choice(['cad', 'usd'])

        user_type = random.choice(UserType.objects.all())

        user = User.objects.create(
            user_type=user_type,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            avatar=avatar,
            availability=random.uniform(0.0, 24.0),
            is_active=True,
            is_superuser=False,
            is_staff=False,
            is_admin=False,
            bio=bio,
            gender=gender,
            currency_code=currency_code
        )

        # Add random addresses to users
        user.address = random.choice(Address.objects.all())
        user.save()

    print('Dummy data created successfully')

if __name__ == "__main__":
    create_dummy_data()
