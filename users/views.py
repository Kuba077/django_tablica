from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse

from users.forms import UserLoginForm


def wyloguj(request):
    logout(request)
    messages.info(request, "Zostałeś wylogowany!")
    return redirect(reverse('tablica:post_lista'))


def rejestruj(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Konto utworzono!")
            return redirect(reverse("tablica:post_lista"))

    else:
        form = UserCreationForm()

    kontekst = {'form': form}
    return render(request, 'users/rejestruj.html', kontekst)


def loguj(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            nazwa = form.cleaned_data['login']
            haslo = form.cleaned_data['haslo']
            user = authenticate(request, username=nazwa, password=haslo)
            if user is not None:
                login(request, user)
                messages.success(request, "Zostałeś zalogowany")
                return redirect(reverse("tablica:post_lista"))
            else:
                messages.error(request, "Błędny login, lub hasło")

    else:
        form = UserLoginForm()

    kontekst = {'form': form}
    return render(request, 'users/loguj.html', kontekst)
