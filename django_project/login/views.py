from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate,
    login as auth_login,
    logout as auth_logout
)
from django.views.decorators.http import require_POST
from .forms import LoginForm


def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            username = login_form.cleaned_data['login']
            password = login_form.cleaned_data['password']

            user = authenticate(
                # Проверяет, существует ли пользователь с таким логином и правильным паролем.
                request,
                username=username,
                password=password
            )

            if user is not None:
                # Выполняет вход пользователя в систему, сохраняя его авторизацию в сессии.
                auth_login(request, user)
                return redirect('home')
            else:
                login_form.add_error(
                    # Добавляет общую ошибку формы, если логин или пароль неправильные.
                    None,
                    'Неверный логин или пароль'
                )

    else:
        login_form = LoginForm()

    context = {'login_form': login_form}
    return render(request, 'login.html', context)

@require_POST
def logout(request):
    auth_logout(request)
    return redirect('home')