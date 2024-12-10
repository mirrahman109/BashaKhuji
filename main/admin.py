from django.contrib import admin
from .models import PropertyDetails, AddressDetails, PropertyImage,UserDetails

@admin.register(PropertyDetails)
class PropertyDetailsAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'bedrooms', 'bathrooms', 'size', 'availability_date', 'created_at')
    search_fields = ('title', 'price')
    list_filter = ('price', 'bedrooms', 'bathrooms', 'availability_date')

@admin.register(AddressDetails)
class AddressDetailsAdmin(admin.ModelAdmin):
    list_display = ('property', 'street', 'city', 'state', 'zip_code')
    search_fields = ('street', 'city', 'state', 'zip_code')
    list_filter = ('city', 'state')

admin.site.register(PropertyImage)
admin.site.register(UserDetails)