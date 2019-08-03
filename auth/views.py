from django.shortcuts import render
from main import models
from django.contrib.auth.views import (
    LoginView,
    LogoutView as Logout
)
from django.views.generic import CreateView
# Create your views here.

class Login(LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True

class SignUp(CreateView):
    model = models.User
    template_name = 'auth/signup.html'
    fields = '__all__'
    success_url = '/'