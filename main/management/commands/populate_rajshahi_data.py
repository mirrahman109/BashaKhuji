import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from main.models import UserDetails, PropertyDetails, AddressDetails

class Command(BaseCommand):
    help = 'Populate database with 50 users and properties in Rajshahi city, Bangladesh'

    def handle(self, *args, **kwargs):
        # Create 50 users and user details
        for i in range(1, 51):
            username = f"user{i}"
            email = f"user{i}@example.com"
            password = "password123"

            # Create Django user
            user, created = User.objects.get_or_create(username=username, email=email)
            if created:
                user.set_password(password)
                user.save()

            # Create UserDetails
            user_details, _ = UserDetails.objects.get_or_create(
                user=user,
                defaults={
                    "name": f"User {i}",
                    "email": email,
                    "address": "Rajshahi, Bangladesh",
                    "contact_number": f"017{i:08d}"
                }
            )

        self.stdout.write(self.style.SUCCESS("50 users created successfully."))

        # Create 50 properties for Rajshahi
        streets = [
            "Bhadra", "Rajshahi Court", "Kazla", "Shiroil", "Motihar", 
            "Ghoramara", "Sopura", "Binodpur", "Railgate", "Sadhur Mor"
        ]
        for i in range(1, 51):
            owner = UserDetails.objects.order_by("?").first()  # Assign a random owner

            # Create PropertyDetails
            property_details, _ = PropertyDetails.objects.get_or_create(
                title=f"Property {i} in Rajshahi",
                defaults={
                    "price": random.randint(5000, 50000),
                    "bedrooms": random.randint(1, 5),
                    "bathrooms": random.randint(1, 3),
                    "size": random.randint(500, 2500),
                    "availability_date": datetime.now() + timedelta(days=random.randint(1, 60)),
                    "owner_details": owner
                }
            )

            # Create AddressDetails
            street = random.choice(streets)
            AddressDetails.objects.get_or_create(
                property=property_details,
                defaults={
                    "street": f"{street} Road",
                    "city": "Rajshahi",
                    "state": "Rajshahi",
                    "zip_code": f"{random.randint(6000, 6100)}"
                }
            )

        self.stdout.write(self.style.SUCCESS("50 properties added for Rajshahi."))
