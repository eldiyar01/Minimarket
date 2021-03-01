from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from .models import User
from .forms import SignInForm, SignUpForm, UpdateUserForm


class SignIn(LoginView):
    form_class = SignInForm
    template_name = 'users/sign_in.html'


class SignOut(LogoutView):
    template_name = 'user/login.html'


class SignUp(CreateView):
    template_name = 'users/sign_up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('users:sign_in')


class Profile(UpdateView):
    template_name = 'users/profile.html'
    form_class = UpdateUserForm

    def get_queryset(self):
        return User.objects.all()