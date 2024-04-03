import random
import string
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from user.models import User, UserType, Address
from service.models import *

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))
#
# def generate_dummy_users(num_users=10):
#     for _ in range(num_users):
#         first_name = generate_random_string(8)
#         last_name = generate_random_string(8)
#         email = f"{first_name.lower()}.{last_name.lower()}@gmail.com"
#         phone_number = ''.join(random.choices(string.digits, k=10))  # Random phone number
#         username = f"{first_name.lower()}_{last_name.lower()}"
#         password = generate_random_string(10)
#         user_type = UserType.objects.first()  # Assuming you have a UserType model with data
#
#         # Create a user instance with random data
#         user = User.objects.create(
#             first_name=first_name,
#             last_name=last_name,
#             username=username,
#             email=email,
#             phone_number=phone_number,
#             user_type=user_type,
#             password=make_password(password),  # Hash the password
#             created_at=timezone.now(),
#             updated_at=timezone.now(),
#             is_active=True,
#             is_staff=False,
#             is_superuser=False,
#             email_verified=True,  # Set to True for dummy data
#         )
#
#         # Optionally, create an Address instance and link it to the user
#         address = Address.objects.create(
#             add1="123 Main St",
#             city="Windsor",
#             provision="Ontario",
#             country="Canada",
#             postal_code="N9A 5E3",
#         )
#         user.address = address
#         user.save()
#
#         print(f"Created user: {user}")
#
# # Call the function to generate dummy users
# generate_dummy_users(10)
#
#
#
# def generate_dummy_service_categories(num_categories=7):
# 	categories = ['Fitness & Wellness','Home Services','Food & Catering','Beauty & Personal Care','Education & Tutoring','Automotive Services','Healthcare & Medical']
# 	for cat in categories:
# 		category = ServiceCategory.objects.create(name=cat,)
# 		print(f"Created category: {category}")
#
# # Call the function to generate dummy service categories
# generate_dummy_service_categories(5)



def generate_dummy_provider_services(num_services=10):
    categories = ServiceCategory.objects.all()
    providers = User.objects.filter(user_type__user_type='provider')
    addresses = Address.objects.all()
    titles = ['Yoga Classes','House Cleaning','Personal Chef Services','Haircut and Styling','Math Tutoring','Car Wash and Detailing','Mental Health Counseling']
    for title in titles:
        title = title  # Generate a random title for the service
        category = random.choice(categories)
        provider = random.choice(providers)
        price = random.uniform(10, 100)
        desc = generate_random_string(50)
        address = random.choice(addresses)
        service = ProviderService.objects.create(
            title=title,
            category=category,
            provider=provider,
            price=price,
            active=True,
            desc=desc,
            address=address
        )
        print(f"Created service: {service}")

# Call the function to generate dummy provider services
generate_dummy_provider_services(10) 





