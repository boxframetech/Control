from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import JournalModel,DebtorModel
from .forms import JournalForm, DebtorForm
from django.views.decorators.http import require_http_methods

# Create your views here.
class JournalList(ListView):
    queryset = JournalModel.objects.all()
    template_name = 'journal/display_journal.html'


class JournalAdd(CreateView):
    form_class = JournalForm
    template_name = 'form.html'
    success_url = '/finance/'


@require_http_methods(['DELETE'])
def delete_journal(request,id):
    JournalModel.objects.filter(id=id).delete()
    queryset = JournalModel.objects.all()
    return render(request,'journal/journals_list.html',{'object_list':queryset})


# DEBTORS

class DebtorList(ListView):
    queryset = DebtorModel.objects.all()
    template_name = 'debtors/display_debtor.html'


class DebtorAdd(CreateView):
    form_class = DebtorForm
    template_name = 'form.html'
    success_url = '/finance/'


@require_http_methods(['DELETE'])
def delete_debtor(request,slug):
    DebtorModel.objects.filter(slug=slug).delete()
    queryset = DebtorModel.objects.all()
    return render(request,'debtors/debtors_list.html',{'object_list':queryset})



def search(request):
    queryset = JournalModel.objects.all()

    if 'description' in request.GET:
        description = request.GET['description']
        if description:
            queryset = queryset.filter(description__icontains=description)
    
    
    if 'amount' in request.GET:
        amount = request.GET['amount']
        if amount:
            queryset = queryset.filter(amount__iexact=amount)
    
    context = {
        'journals':queryset
    }
    
    return render(request,'search.html',context)