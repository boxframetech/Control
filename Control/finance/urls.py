from django.urls import path

from django.views.generic import TemplateView
from .views import JournalList, JournalAdd,delete_journal, DebtorAdd, DebtorList,delete_debtor,search

urlpatterns = [
    path('', TemplateView.as_view(template_name='finance_dashboard.html'), name='finance-dashboard'),
    path('journals', JournalList.as_view(), name='journal-list'),    
    path('addjournal', JournalAdd.as_view(), name='journal-add'), 
    path('<int:id>/delete/', delete_journal, name='delete_journal'),


    # Debtors
    path('debtors', DebtorList.as_view(), name='debtor-list'),    
    path('adddebtor', DebtorAdd.as_view(), name='debtor-add'), 
    path('<str:slug>/delete/', delete_debtor, name='delete_debtor'),

    path('search', search, name='search')

    
]
