from django.urls import path

from django.views.generic import TemplateView
from .views import StudentList,StudentAdd

urlpatterns = [
    path('', TemplateView.as_view(template_name='officeadmin_dashboard.html'), name='admin-dashboard'),    
    path('student', StudentList.as_view(), name='student-list'),    
    path('addstudent', StudentAdd.as_view(), name='student-add'), 
    # path('<int:id>/delete/', delete_journal, name='delete_journal'),


    # # Debtors
    # path('debtors', DebtorList.as_view(), name='debtor-list'),    
    # path('adddebtor', DebtorAdd.as_view(), name='debtor-add'), 
    # path('<str:slug>/delete/', delete_debtor, name='delete_debtor'),

    # path('search', search, name='search')
]
