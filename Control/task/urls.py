from django.urls import path
from .views import delete_task, display_task

urlpatterns = [
    path('displaytask', display_task, name='home'),  
    path('<int:id>/delete/', delete_task, name='delete_task')
]