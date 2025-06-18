from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView 
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

class TeacherDetialView(DetailView):
    model = Teacher
    template_name = 'teachers/teacher_detial.html'
    context_object_name = 'teacher'

class TeacherUpdateView(UpdateView):
    model = Teacher
    template_name = 'teachers/teacher_form.html'
    fields = ['full_name', 'email', 'dpartment', 'phone_no', 'join_date', 'user']
    success_url = 'teacher.index'

class TeacherDeleteView(DeleteView):
    model = Teacher
    context_object_name = 'teacher'
    template_name = 'teachers/teacher_delete_confirm.html'
    success_url = 'teacher.index'

# class StudentListView(ListView):
#     model = Student
#     context_object_name = 'student'
#     template_name = 'students/students_index.html'
#     paginate_by = 5
