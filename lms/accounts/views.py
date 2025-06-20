from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'students/profile.html'

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')