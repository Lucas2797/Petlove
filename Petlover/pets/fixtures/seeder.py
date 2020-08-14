from django.core.management.base import BaseCommand
from ..models import People, Pets
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify

User = get_user_model()

'''
class GenerateUser():
    username = None
    password = None
    def __init__(self, username, password):
        with open('User.txt') as file_name:
            for rows in file_name:
                self.username = slugify(rows)
                self.password = '12345'

                   
class GeneratePeople():
    user = None
    documento = None
    birthday = None
    def __init__(self, documento, birthday):
        with open('People.txt') as file_name:
            for rows in file_name:
                t1 = rows.split(', ')
                self.user = slugify(t1[0])
                self.documento = t1[1]
                self.birthday = t1[2]
'''


class Command(BaseCommand):


    def handle(self, *args, **kwargs):

        with open('People.txt') as file:
            for row in file:
                spl = row.split(', ')
                s1 = slugify(spl[1])


        one =  User(
            username = s1,
            password = 'lukasfaria',
            email = 'lucas.reimol@gmail.com'
        )

        one.save()

        
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
'''
        peop = People(
            user=user,
            documento=documento,
            birthday=birthday
        )

        peop.save()
'''
