from django.core.management.base import BaseCommand
from ...models import People, Pets
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from decimal import Decimal

User = get_user_model()


class Command(BaseCommand):


    def handle(self, *args, **kwargs):
        
        
        
        CACHORRO = 1
        GATO = 2
        ANDORINHA = 3
        PAPAGAIO = 4
        IGUANA = 5
        CAVALO = 6
        ORNITORRINCO = 7
        LHAMA = 8

        dict1 = {
            'CACHORRO' : 1,
            'GATO' : 2,
            'ANDORINHA' : 3,
            'PAPAGAIO' : 4,
            'IGUANA' : 5,
            'CAVALO' : 6,
            'ORNITORRINCO' : 7,
            'LHAMA' : 8,
        }

        with open('Animais.txt') as file:
            for row in file:
                spl = row.split(', ')
                slug1 = slugify(spl[3])
                price_in_decimal = Decimal(spl[1].replace(',','.'))
                key_dict = spl[2].upper()

                pet = Pets(
                    pessoa = People.objects.get(user__username__exact=slug1),
                    nome = spl[0],
                    custo = price_in_decimal,
                    tipo = dict1[key_dict]
                )

                pet.save()
                self.stdout.write(self.style.SUCCESS('Data imported successfully'))