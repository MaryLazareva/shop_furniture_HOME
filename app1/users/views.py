from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import HttpResponseRedirectBase
from django.shortcuts import redirect, render
from django.urls import reverse


from users.forms import ProfileForm, UserLoinForm, UserRegistrationForm


def login(request):
    if request.method == 'POST':
        form = UserLoinForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, Вы вошли в аккаунт")
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoinForm()
    context = {
            "title": "Home - Авторизация",
            "form": form,
            }
    return render(request, "users/login.html", context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            # Чтобы прирегистрации стразу заходить в личный кабинет без введения своих данных снова
            user = form.instance
            auth.login(request, user)
            messages.success(request, f"{user.username}, Вы успешно зарагистрированы и вошли в аккаунт")
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()

    context = {
            "title": "Home - Регистрация",
            "form": form,
            }
 
    return render(request, "users/registration.html", context)

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES) # используем instance, для какого пользователя нужно сохранять информацию
        if form.is_valid():
            form.save()
            messages.success(request, "Профайл успешно обновлен")
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        # добавляем instance, чтобы была информация, которая за ним числилась
        form = ProfileForm(instance=request.user)

    context = {
            "title": "Home - Кабинет",
            "form": form,
            }
 
    return render(request, "users/profile.html", context)

@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, Вы вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse('main:index'))

