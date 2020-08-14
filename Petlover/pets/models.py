from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.validators import RegexValidator
from django.http import request
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import request


User = get_user_model()



class People(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='person')
    birthday = models.DateField()
    cpf = models.CharField(max_length=11, validators=[RegexValidator(r'^\d{1,10}$')])

    def __str__(self):
        return '%s' % (self.user)


class Pets(models.Model):
    pessoa = models.ForeignKey(People, on_delete=models.CASCADE, related_name='peop')
    nome = models.CharField(max_length=150)
    custo = models.DecimalField(max_digits=7, decimal_places=2)
    tipo = models.SmallIntegerField()


    def __str__(self):
        return '%s - %s' % (self.pessoa, self.nome)

'''    
    def clean_fields(self, exclude=None):
        super().clean_fields(exclude=exclude)
        slug = slugify(self.pessoa)
        if slug.startswith('a') and self.tipo == 2:
            if exclude and 'pessoa' in exclude:
                raise ValidationError('pessoas com a nao podem ter gatos')
'''
