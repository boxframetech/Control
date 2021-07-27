from django.forms import ModelForm, fields
from .models import StudentsModel

class StudentForm(ModelForm):
    class Meta:
        model = StudentsModel
        fields = '__all__'
