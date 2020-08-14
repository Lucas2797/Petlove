from django.core.management.base import BaseCommand
from ...models import People, Pets
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify

User = get_user_model()


class Command(BaseCommand):


    def handle(self, *args, **kwargs):

        with open('People.txt') as file:
            for row in file:
                spl = row.split(', ')
                s1 = slugify(spl[0])
                email = '{}.gmail.com'.format(s1)
                s2 = s1.split('-')
                first = s2[0]
                second = s2[1]


                one =  User(
                    username = s1,
                    password = 'reimol',
                    email = email,
                    first_name = first,
                    last_name = second
                )

                one.save()
                
                peop = People(
                    user = one,
                    birthday = spl[2],
                    cpf = spl[1] 
                )

                peop.save()
        
                self.stdout.write(self.style.SUCCESS('Data imported successfully'))


'''
        peop = People(
            user=user,
            documento=documento,
            birthday=birthday
        )

        peop.save()
'''

































'''
class GenerateUser():
    username = None
    password = None
    def __init__(self, username, password):
        with open('User.txt') as file:
            for rows in file:
                self.username = slugify(rows)
                self.password = '123456789'

                   
class GeneratePeople():
    user = None
    cpf = None
    birthday = None
    def __init__(self, documento, birthday):
        with open('People.txt') as file:
            for rows in file:
                t1 = rows.split(', ')
                self.user = slugify(t1[0])
                self.cpf = t1[1]
                self.birthday = t1[2]


class Command(BaseCommand):


    def handle(self, *args, **kwargs):

        user = GeneratePeople.user
        cpf = GeneratePeople.cpf
        birthday = '2012-04-12'


        peop = People(
            user=user,
            cpf=cpf,
            birthday=birthday
        )

        peop.save()


        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
'''