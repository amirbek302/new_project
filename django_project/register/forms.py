from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        label='Имя:',
        max_length=100
    )

    username = forms.CharField(
        label='Логин:',
        max_length=150,
        help_text=''
    )

    email = forms.EmailField(
        label='Email:'
    )

    age = forms.IntegerField(
        label='Возраст:',
        min_value=1,
        max_value=103
    )

    work = forms.ChoiceField(
        label='Работа:',
        choices=[
            ('Работает', 'Работает'),
            ('Безработный', 'Безработный'),
            ('Студент', 'Студент')
        ]
    )

    hobby = forms.MultipleChoiceField(
        label='Увлечения:',
        choices=[
            ('Игры', 'Игры'),
            ('Спорт', 'Спорт'),
            ('Еда', 'Еда'),
            ('Танцы', 'Танцы')
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    password1 = forms.CharField(
        label='Пароль:',
        min_length=8,
        widget=forms.PasswordInput
    )

    # что-бы переспрашивать пароль

    password2 = forms.CharField(
        label='Подтверждение пароля:',
        widget=forms.PasswordInput
    )

    class Meta(UserCreationForm.Meta):
        model = User
        # наша модель пользователя из models.py.

        fields = [
            'first_name',
            'username',
            'email',
            'age',
            'work',
            'hobby'
        ]