from django.core.management.base import BaseCommand
from faker import Faker
from main.models import PropertyDetails, AddressDetails
from datetime import datetime

class Command(BaseCommand):
    help = 'Populate the database with 500 property and address details'

    def handle(self, *args, **kwargs):
        fake = Faker()
        property_list = []
        address_list = []

        for _ in range(500):
            property = PropertyDetails(
                title=fake.company(),
                image_url=fake.image_url(),
                price=fake.random_number(digits=6),
                bedrooms=fake.random_int(min=1, max=5),
                bathrooms=fake.random_int(min=1, max=3),
                size=fake.random_int(min=500, max=5000),
                availability_date=fake.date_between(start_date='today', end_date='+1y'),
                created_at=datetime.now()
            )
            property_list.append(property)

            address = AddressDetails(
                property=property,  # Link to the property
                street=fake.street_address(),
                city=fake.city(),
                state=fake.state(),
                zip_code=fake.zipcode()
            )
            address_list.append(address)

        # Bulk create instances
        PropertyDetails.objects.bulk_create(property_list)
        AddressDetails.objects.bulk_create(address_list)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with 500 properties and addresses'))
