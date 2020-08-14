from django import forms
from .models import Pets, People
from django.http import request
from django.template.defaultfilters import slugify
from django.forms import ValidationError
from datetime import date
from django.contrib.auth import get_user_model
from django.db.models import F, DurationField


User = get_user_model()

class PetForm(forms.ModelForm):  #create_pet_template, create_pet_view, create_pet_view2, create_pet_form3
    class Meta:
        prefix = 'pet'
        model = Pets
        fields = ['pessoa', 'nome', 'custo', 'tipo']


class PeopleForm(forms.ModelForm):
    birthday = forms.DateField()
    cpf = forms.CharField(max_length=12)

    class Meta:
        prefix = 'peop'
        model = People
        fields = ['birthday', 'cpf']
