from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import HttpResponseRedirectBase
from django.shortcuts import render
from django.urls import reverse

from users.forms import UserLoinForm


def login(request):
    if request.method == 'POST':
        form = UserLoinForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoinForm()
    context = {
            "title": "Home - Авторизация",
            "form": form,
            }
    return render(request, "users/login.html", context)


def registration(request):
    context = {"title": "Home - Регистрация"}
    return render(request, "users/registration.html", context)


def profile(request):
    context = {"title": "Home - Кабинет"}
    return render(request, "users/profile.html", context)


def logout(request): ...
