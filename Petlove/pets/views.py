from django.shortcuts import render, redirect
from .models import Pets, People
from django.contrib.auth.decorators import login_required
from .forms import PetForm
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

def create_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PetForm()

    context = {'form': form}

    return render (request, 'petform.html', context)

