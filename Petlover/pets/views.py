from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import Pets, People
from django.contrib.auth.decorators import login_required
from .forms import PetForm1, PetForm2, PeopleForm, PetForm3, PetForm4, PetForm5
from django.db import transaction
from django.contrib import messages
from django.contrib.auth import get_user_model
from datetime import date
from django.db.models import F, ExpressionWrapper, DurationField
from django.forms import ValidationError
from django.template.defaultfilters import slugify
from django.db.models import Sum


User = get_user_model()

def home_view(request):

    #Qual é o custo médio dos animais do tipo cachorro?
    q1 = Pets.objects.filter(tipo=1)
    custo_total = 0
    for q in q1:
        custo_total += q.custo
    media = custo_total/q1.count()
    #Quantos cachorros existem no sistema?
    q2 = Pets.objects.filter(tipo=1)
    quant = q2.count()
    #Qual o nome dos donos dos cachorros (Array de nomes)
    q3 = Pets.objects.all()
    nomes = []
    for p in q3:
        nome = p.pessoa.user.username
        if p.tipo == 1:
            if nome in nomes:
                pass
            else:
                nomes.append(nome)

    #Retorne as pessoas ordenando pelo custo que elas tem com os animais (Maior para menor)
    t1 = Pets.objects.values('pessoa__user__username').annotate(soma=Sum('custo')).order_by('-soma')

    #Levando em consideração o custo mensal, qual será o custo de 3 meses de cada pessoa?
    t2 = Pets.objects.values('pessoa__user__username').annotate(soma=Sum('custo') * 3)
    context = {
        #1 pergunta
        'media': media,
        #2 pergunta
        'quant': quant,
        #3 pergunta
        'nomes': nomes,
        #4 pergunta
        't1': t1,
        #5 pergunta
        't2': t2
    }
    return render (request, 'home.html', context)




#SELECIONAR O FORM PELO TEMPLATE
@login_required
@transaction.atomic
def create_pet_template(request):
    if request.method == 'POST':
        form = PetForm1(request.POST) # COM GATO
        form2 = PetForm2(request.POST) #sem GATO
                                        #Com gato -18
                                        #sem gato +18
        if form.is_valid() or form2.is_valid():
            pet = form.save(commit=False) or form2.save(commit=False)
            pet.pessoa = request.user.person
            pet.save()
    else:
        form = PetForm1()
        form2 = PetForm2()
    context = {
        'form': form,
        'form2': form2
    }

    return render(request, 'petform.html', context)
    


#SELECIONAR O FORM PELA VIEW
@login_required
@transaction.atomic
def create_pet_view(request):
    no_cat_people = User.objects.filter(username__istartswith='a')
    if request.user in no_cat_people:
        if request.method == 'POST':
            form = PetForm2(request.POST) # Sem gato
            pet = form.save(commit=False)
            pet.pessoa = request.user.person
            pet.save()
        else:
            form = PetForm2()
    else:
        if request.method == 'POST':
            form = PetForm1(request.POST) # Com gato
            pet = form.save(commit=False)
            pet.pessoa = request.user.person
            pet.save()
        else:
            form = PetForm1()
    context = {
        'form': form,
    }

    return render(request, 'petform2.html', context)

#Raising a validation on Views
def create_pet_view2(request, *args, **kwargs):
    if request.method == 'POST':
        form = PetForm1(request.POST)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.pessoa = request.user.person
            slug = slugify(pet.pessoa)
            if slug.startswith('a') and pet.tipo == 2 :
                raise ValidationError('pessoas com A inicial nao podem ter gatos')
            pet.save()
    else:
        form = PetForm1(request.POST)
    context = {
        'form': form
        }
    return render(request, 'petform3.html', context)


def create_pet_form(request):
    d=0
    P1 = People.objects.get(user=request.user.id)
    for p in Pets.objects.filter(pessoa=P1.id):
        c = p.custo
        d = d+c
    if d >= 1000:
        raise ValidationError('Valor {} passa do limite 1000'.format(d))
    if request.method == 'POST':
        form = PetForm3(request.POST,)
        if form.is_valid():
            form.save()
    else:
        form = PetForm3(request.POST)
    context = {
        'form': form
        }
    return render(request, 'petform4.html', context)

@login_required
def create_pet_form2(request):
    if request.method == 'POST':
        form = PetForm4(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PetForm4()

    context = {'form': form}

    return render (request, 'petform4.html', context)







@login_required
def create_people(request):
    if request.method == 'POST':
        form = PeopleForm(request.POST)
        if form.is_valid():
            peop = form.save(commit=False)
            peop.user = request.user
            peop.save()
            return redirect('/')
        else:
            messages.error(request, ('corrrija os erros'))
    else:
        form = PeopleForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'peopleform.html', context)


def test_birthday(request):
    today = date.today()
    set_date = People.objects.get(user=request.user.id)
    set_date2 = set_date.birthday
    #delta1 = ExpressionWrapper(today - set_date2, output_field=DurationField())
    delta2 = today - set_date2 
    #ages_detector = People.objects.filter(birthday__lte=delta2)
    if delta2.days >= 6570:
        if request.method == 'POST':
            form = PetForm2(request.POST) # Sem gato
            pet = form.save(commit=False)
            pet.pessoa = request.user.person
            pet.save()
        else:
            form = PetForm2()
    else:
        if request.method == 'POST':
            form = PetForm1(request.POST) # Com gato
            pet = form.save(commit=False)
            pet.pessoa = request.user.person
            pet.save()
        else:
            form = PetForm1()
    context={
        'form': form
    }
    return render(request, 'test_birthday.html', context)



def create_pet_form3(request):
    if request.method == 'POST':
        form = PetForm5(request.POST)
        form.pessoa = request.user.person
        if form.is_valid():
            form.save()
    else:
        form = PetForm5()
    context = {
        'form': form
    }
    return render(request, 'petform2.html', context)
