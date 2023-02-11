from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView
from .models import District
from .forms import RegisterForm, AccountApplicationForm
# Create your views here.

class HomeView(CreateView):
    template_name = "home.html"
    form_class = AccountApplicationForm
    success_url = 'success'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data()
        context['branches'] = District.objects.all()
        return context


class MyLoginView(LoginView):
    template_name = "login.html"

    def get_context_data(self, **kwargs):
        context = super(MyLoginView, self).get_context_data()
        context['branches'] = District.objects.all()
        return context


class SuccessView(TemplateView):
    template_name = "success.html"

    def get_context_data(self, **kwargs):
        context = super(SuccessView, self).get_context_data()
        context['branches'] = District.objects.all()
        return context


class RegistrationView(CreateView):
    template_name = "register.html"
    form_class = RegisterForm
    success_url = 'login'

    def get_context_data(self, **kwargs):
        context = super(RegistrationView, self).get_context_data()
        context['branches'] = District.objects.all()
        return context