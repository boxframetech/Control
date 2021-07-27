from django.shortcuts import render
from .models import Task
from django.views.decorators.http import require_http_methods
# Create your views here.

def display_task(request):
    task = Task.objects.all()
    return render(request, 'display_task.html',{'tasks':task})

@require_http_methods(['DELETE'])
def delete_task(request,id):
    Task.objects.filter(id=id).delete()
    tasks = Task.objects.all()
    return render(request,'tasks_list.html',{'tasks':tasks})