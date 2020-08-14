from django.urls import path
from . import views



urlpatterns = [
    path('home/', views.home_view, name='home'),
    #template
    path('pet_create/', views.create_pet_template, name='add_pet'),
    #view
    path('pet_create2/', views.create_pet_view, name='add_pet2'),
    #form
    path('pet_create3/', views.create_pet_view2, name='add_pet3'),
    path('pet_create4/', views.create_pet_form, name='add_pet4'),
    path('pet_create5/', views.create_pet_form2, name='add_pet5'),
    #model
    path('pet_create6/', views.create_pet_form3, name='add_pet6'),
    path('test_birthday/', views.test_birthday, name='test_birthday'),
]
