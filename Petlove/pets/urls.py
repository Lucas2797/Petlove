from django.urls import path
from . import views



urlpatterns = [
    path('home/', views.home_view, name='home'),
    #template
    path('pet_create/', views.create_pet, name='add_pet'),
]
