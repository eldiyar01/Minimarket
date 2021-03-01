from django.contrib.auth import password_validation
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField, UserChangeForm
from django import forms
from django.forms import CharField

from .models import User


class SignUpForm(UserCreationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control mt-2',
                                                           'placeholder': 'Create a username'}))
    first_name = CharField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control mt-2',
                                                         'placeholder': 'Your first name'}))
    last_name = CharField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control mt-2',
                                                        'placeholder': 'Your last name'}))
    password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control mt-2',
                                          'placeholder': 'Create a password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control mt-2',
                                          'placeholder': 'Confirm the password'}),
        strip=False,
        help_text=("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')


class SignInForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control mt-2',
                                                           'placeholder': 'Login'}))

    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control mt-2',
                                          'placeholder': 'Your password'}),
    )


class UpdateUserForm(UserChangeForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control mt-2',
                                                           'placeholder': 'Login'}))
    first_name = CharField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control mt-2',
                                                         'placeholder': 'Your first name'}))
    last_name = CharField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control mt-2',
                                                        'placeholder': 'Your last name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')
