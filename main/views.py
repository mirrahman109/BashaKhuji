from django.shortcuts import render, get_object_or_404, redirect
from .models import PropertyDetails, AddressDetails,UserDetails

from django import forms
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserDetails
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm


# View for the homepage
def index(request):
    return render(request, 'index.html')

# View for searching properties based on location and type
def search_properties(request):
    query = request.GET.get('streets', '')
    property_type = request.GET.get('type', '')  # Add property type filtering if needed
    
    properties = PropertyDetails.objects.all()  # Change PropertyListing to PropertyDetails
    if query:
        properties = properties.filter(title__icontains=query)  # Filter by title or other fields
    if property_type:
        properties = properties.filter(property_type=property_type) 
    
    return render(request, 'search_results.html', {'properties': properties})

def all_property(request):
    bedrooms = request.GET.get('bedrooms')
    bathrooms = request.GET.get('bathrooms')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    available_from = request.GET.get('available_from')
    
    # Start with all properties
    properties = PropertyDetails.objects.all()
    
    # Apply filters if criteria are provided
    if bedrooms:
        properties = properties.filter(bedrooms=bedrooms)
    if bathrooms:
        properties = properties.filter(bathrooms=bathrooms)
    if min_price:
        properties = properties.filter(price__gte=min_price)
    if max_price:
        properties = properties.filter(price__lte=max_price)
    if available_from:
        properties = properties.filter(availability_date__gte=available_from)
    
    # Pagination
    paginator = Paginator(properties, 30)
    page_number = request.GET.get('page')
    properties_page = paginator.get_page(page_number)
    
    # Render the page with properties
    return render(request, 'all_property.html', {'properties': properties_page})

def view_details(request, id):
    # Fetch the property by ID
    property_details = get_object_or_404(PropertyDetails, id=id)
    address_details = AddressDetails.objects.get(property=property_details)
    owner_details = property_details.owner_details

    # Fetch the additional images related to the property
    additional_images = property_details.additional_images.all()

    # Pass the data to the template
    context = {
        'property': property_details,
        'additional_images': additional_images,
        'owner_details': owner_details,
        'address': address_details,
    }
    return render(request, 'view_details.html', context)

def signup(request):
    if request.method == 'POST':  
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserDetails.objects.create(
                user=user,
                name=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                contact_number=form.cleaned_data['contact_number']
            )
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()

    return render(request, 'signup.html', {'form': form})

   
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:

        return render(request, 'login.html')

    
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    user_details = get_object_or_404(UserDetails, email=request.user.email)
    properties = PropertyDetails.objects.filter(owner_details=user_details)
    context = {
        'user': user_details,
        'properties': properties,
    }
    return render(request, 'profile.html', context)
