from django.db import models
from django.contrib.auth.models import User

class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField(blank=True, null=True)
    contact_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name or self.email  


class PropertyDetails(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='property_images/', blank=True, null=True) 
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    size = models.IntegerField()
    availability_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    owner_details = models.ForeignKey(UserDetails, on_delete=models.CASCADE, related_name='properties', null=True, blank=True)

    def __str__(self):
        return self.title


class AddressDetails(models.Model):
    property = models.OneToOneField(PropertyDetails, on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}, {self.zip_code}"


class PropertyImage(models.Model):
    property = models.ForeignKey(PropertyDetails, related_name='additional_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images/')

    def __str__(self):
        return f"Image for {self.property.title}"
