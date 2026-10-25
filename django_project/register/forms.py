from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        label='Name:',
        max_length=100
    )

    username = forms.CharField(
        label='Login:',
        max_length=150,
        help_text=''
    )

    email = forms.EmailField(
        label='Email:'
    )

    age = forms.IntegerField(
        label='Age:',
        min_value=1,
        max_value=103
    )

    work = forms.ChoiceField(
        label='Работа:',
        choices=[
            ('Employed', 'Employed'),
            ('Unemployed', 'Unemployed'),
            ('Student', 'Student')
        ]
    )

    hobby = forms.MultipleChoiceField(
        label='Увлечения:',
        choices=[
            ('Games', 'Games'),
            ('Sport', 'Sport'),
            ('Food', 'Food'),
            ('Dance', 'Dance')
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    password1 = forms.CharField(
        label='Password:',
        min_length=8,
        widget=forms.PasswordInput
    )

    # что-бы переспрашивать пароль

    password2 = forms.CharField(
        label='Confirm password:',
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