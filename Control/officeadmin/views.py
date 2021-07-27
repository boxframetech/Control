from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.views.decorators.http import require_http_methods
from .models import OfficialDoc,SpacesModel,SpaceusersModel,Facilitator,StudentsModel
from .forms import StudentForm


# Create your views here.
class StudentList(ListView):
    queryset = StudentsModel.objects.all()
    template_name = 'students/display_student.html'


class StudentAdd(CreateView):
    form_class = StudentForm
    template_name = 'form.html'
    success_url = '/administration/'

