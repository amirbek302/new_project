from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import RegisterForm


def register(request):
    if request.method == 'POST':
        reg_form = RegisterForm(request.POST)

        if reg_form.is_valid():
            user = reg_form.save()

            auth_login(request, user)
            # Пользователю не нужно повторно вводить логин и пароль после регистрации.

            return redirect('home')

    else:
        reg_form = RegisterForm()

    context = {'reg_form': reg_form}

    return render(request, 'register.html', context)