from django.forms import ModelForm, fields
from .models import JournalModel,DebtorModel

class JournalForm(ModelForm):
    class Meta:
        model = JournalModel
        fields = ['cr_account','dr_account','name','amount','description','docs','is_payable','is_receivable',
        'bank_activity','is_taxwitheld'
        ]

class DebtorForm(ModelForm):
    class Meta:
        model = DebtorModel
        fields = [ 'name','slug','phone','service_rendered','location']