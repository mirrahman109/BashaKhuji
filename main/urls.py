from django.contrib import admin
from django.urls import path,include
from main import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("",views.index, name = 'home'),
    path("all_property",views.all_property, name = 'all_property'),
    path("about",views.index, name = 'about'),
    path("contact",views.index, name = 'contact'),
    path('search/', views.search_properties, name='search'),
    path('property/<int:id>/', views.view_details, name='view_details'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
     path('profile/', views.profile, name='profile'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)