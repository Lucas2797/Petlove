from django import forms
from .models import Pets, People
from django.http import request
from django.template.defaultfilters import slugify
from django.forms import ValidationError
from datetime import date
from django.contrib.auth import get_user_model
from django.db.models import F, DurationField


User = get_user_model()

class PetForm1(forms.ModelForm):  #create_pet_template, create_pet_view, create_pet_view2, create_pet_form3
    field_choices = [
        (1, 'CACHORRO'),
        (2, 'GATO'),
        (3, 'ANDORINHA')
    ]

    nome = forms.CharField(max_length=100)
    custo = forms.DecimalField(max_digits=7, decimal_places=2)
    tipo = forms.ChoiceField(choices=field_choices)

    class Meta:
        prefix = 'pet'
        model = Pets
        fields = ['nome', 'custo', 'tipo']


class PetForm2(forms.ModelForm):  #create_pet_template, create_pet_view
    field_choices_subset = [
        (1, 'CACHORRO'),
        (3, 'OUTRO'),
    ]

   # def __init__(self, *args, **kwargs):
    #    super().__init__(*args, **kwargs)

    #    if kwargs.get("instance") and kwargs.get("instance").pessoa.nome.startswith("a"):
    #        self.fields["tipo"].choices = field_choices_subset

    nome = forms.CharField(max_length=150)
    custo = forms.DecimalField(max_digits=7, decimal_places=2)
    tipo = forms.ChoiceField(choices=field_choices_subset)

    class Meta:
        prefix = 'pet'
        model = Pets
        fields = ['nome', 'tipo', 'custo']    





class PetForm3(forms.ModelForm):        #create_pet_form
    field_choices = [
        (1, 'CACHORRO'),
        (2, 'GATO'),
        (3, 'ANDORINHA')
    ]

    nome = forms.CharField(max_length=100)
    custo = forms.DecimalField(max_digits=7, decimal_places=2)
    tipo = forms.ChoiceField(choices=field_choices)


    class Meta:
        prefix = 'pet'
        model = Pets
        fields = ['pessoa' ,'nome', 'custo', 'tipo']


    def clean_tipo(self):
        data = self.cleaned_data.get("tipo")
        pk = self.cleaned_data.get("pessoa")
        P = People.objects.get(pk=pk.id)
        delta = date.today() - P.birthday
        slug = slugify(pk)
        if slug.startswith('a') and data == '2':
            raise forms.ValidationError('nomes com A nao podem ter gatos')
        if delta.days <= 6570 and data == '3':
            raise forms.ValidationError('menores de 18 nao podem ter andorinhas')
        return data


class PetForm4(forms.ModelForm):        #create_pet_form2
    field_choices = [
        (1, 'CACHORRO'),
        (2, 'GATO'),
        (3, 'ANDORINHA'),
        (4, 'PAPAGAIO'),
        (5, 'IGUANA'),
        (6, 'CAVALO'),
        (7, 'ORNITORRINCO'),
        (8, 'LHAMA')
    ]

    nome = forms.CharField(max_length=100)
    custo = forms.DecimalField(max_digits=7, decimal_places=2)
    tipo = forms.ChoiceField(choices=field_choices)


    class Meta:
        prefix = 'pet'
        model = Pets
        fields = ['pessoa' ,'nome', 'custo', 'tipo']


    def clean_tipo(self):
        data = self.cleaned_data.get("tipo")
        pk = self.cleaned_data.get("pessoa")
        P = People.objects.get(pk=pk.id)
        delta = date.today() - P.birthday
        slug = slugify(pk)
        if slug.startswith('a') and data == '2':
            raise forms.ValidationError('nomes com A nao podem ter gatos')
        if delta.days <= 6570 and data == '3':
            raise forms.ValidationError('menores de 18 nao podem ter andorinhas')
        return data

    def clean_custo(self):
        custo_data = self.cleaned_data.get("custo")
        pessoa_data = self.cleaned_data.get("pessoa")
        p1 = Pets.objects.filter(pessoa=pessoa_data)
        soma = 0
        for p in p1:
            d = p.custo
            soma = d + soma
        if soma + custo_data  >= 1000:
            raise ValidationError('desculpe seus custos ultrapassam 1000')
        return custo_data


class PeopleForm(forms.ModelForm):
    birthday = forms.DateField()
    cpf = forms.CharField(max_length=12)

    class Meta:
        prefix = 'peop'
        model = People
        fields = ['birthday', 'cpf']


class PetForm5(forms.ModelForm):
    class Meta:
        prefix = 'pet'
        model = Pets
        fields = ['pessoa', 'nome', 'custo', 'tipo']


    '''
    def clean(self):
        cleaned_data = super(PetForm3, self).clean()
        t1 = User.person.birthday
        bday = t1.birthday
        fraud_detect = F(date.today() - bday, output_field=DurationField())
        if ( (fraud_detect.days / 365.0) < 18 ):
        # WHAT ABOUT THE BABIES!!!!s
            raise forms.ValidationError("Sorry, you cannot create a PET.")
        return cleaned_data
'''

'''
    def clean(self, *args, **kwargs):
        cleaned_data = super(PetForm3, self).clean()
        pessoa_data = self.cleaned_data.get('pessoa')
        pessoa_string = slugify(pessoa_data)
        tipo_data = self.cleaned_data.get('tipo')
        if pessoa_string.startswith('a') and tipo_data==2:
            raise ValidationError('User começando com A não pode ter gato')
        return super(PetForm3, self).clean(*args, **kwargs)

'''