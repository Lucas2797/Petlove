from django.test import TestCase
from django.template.defaultfilters import slugify



def logic():
    name = str(input('seu nome'))
    uppercase = name.upper()
    if uppercase[0] == 'A':
        print(uppercase[0])
        print('ok')





field_choices1 = [
    (1, 'CACHORRO'),
    (2, 'GATO'),
    (3, 'OUTRO')
]

field_choices2 = [
    (1, 'CACHORRO'),
    (3, 'OUTRO')
]

def field_choice2():
    name = str(input('seu nome: '))
    upper = name.upper()
    if upper[0] == 'A':
        print(field_choices1)
    else:
        print(field_choices2)


def field_choice():
    one = str(input('seu nome: '))
    big = one.upper()
    if big[0] == 'A':
        print('2')
        return field_choices2
    else:
        print('1')
        return field_choices1


def test():
    one = 'lucas'
    slug = slugify(one)
    big = slug.upper()
    print(big[0])

test()
