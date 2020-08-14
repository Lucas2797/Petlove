from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError
from datetime import date


User = get_user_model()



class People(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='person')
    birthday = models.DateField()
    cpf = models.CharField(max_length=11, validators=[RegexValidator(r'^\d{1,10}$')])

    def __str__(self):
        return '%s' % (self.user)


class Pets(models.Model):
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
    pessoa = models.ForeignKey(People, on_delete=models.CASCADE, related_name='peop')
    nome = models.CharField(max_length=150)
    custo = models.DecimalField(max_digits=7, decimal_places=2)
    tipo = models.SmallIntegerField(choices=field_choices)


    def __str__(self):
        return '%s - %s' % (self.pessoa, self.nome)

    def clean(self):
        peop = People.objects.get(user__username=self.pessoa)
        all_pets = Pets.objects.filter(pessoa=self.pessoa)
        # gato
        slug = slugify(self.pessoa)
        big = slug.upper()
        # idade
        delta = date.today() - peop.birthday
        # custo
        soma = 0
        for p in all_pets:
            d = p.custo
            soma = d + soma
        if soma + self.custo  >= 1000:
            raise ValidationError('desculpe seus custos ultrapassam 1000')
        #gato
        if big.startswith('A') and self.tipo == 2:
            raise ValidationError('Nomes com A nao podem ter gatos')
        #idade
        if delta.days <= 6570 and self.tipo == 3 :
            raise ValidationError('menores de 18 nao podem ter andorinhas')