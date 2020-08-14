from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from django.urls import reverse
from pets.forms import PeopleForm
from pets.models import People


def login_view (request):
    next = request.GET.get('next')
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('../../pets/home')

    context = {
        'form': form,
    }
    return render(request, "loginform.html", context)

def register_view(request):
    next = request.GET.get('next')
    form = RegisterForm(request.POST or None)
    form2 = PeopleForm(request.POST)
    if form.is_valid() and form2.is_valid():
        usuario = form.save(commit=False)
        password = form.cleaned_data.get('password')
        usuario.set_password(password)
        usuario.save()
        peop = form2.save(commit=False)
        peop.user = usuario
        peop.save()
        new_user = authenticate(username=usuario.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('../../pets/home')

    context = {
        'form': form,
        'form2': form2
    }
    return render(request, "userform.html", context)

def logout_view(request):
    logout(request)
    return redirect ('../login')


