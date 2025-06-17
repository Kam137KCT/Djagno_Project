from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, CreateView
from core.models import Teacher, Student, Assignment, Materials

# Create your views here.
# def home(request):
#     return render(request, 'home.html')

class HomePageView(TemplateView):
    template_name = 'home.html'

class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers/teachers_index.html'
    context_object_name = 'teachers'
    paginate_by = 5

class TeacherCreateView(CreateView):
    model = Teacher
    fields = ['full_name', 'email', 'dpartment', 'phone_no', 'join_date', 'user']
    template_name = 'teachers/teachers_form.html'
    success_url = 'teacher_index'



