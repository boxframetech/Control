from django.contrib import admin
from .models import (
    PettycashModel, PettyCashTransaction,
    JournalModel,DebtorModel,CreditorModel,
    WeeklyProjection
    )
# Register your models here.
class JournalAdmin(admin.ModelAdmin):
    search_fields = ['description','amount','is_payable','is_receivable']
    list_display = ['transaction_date','cr_account','dr_account','name','amount','is_payable','is_receivable',
    'bank_activity','is_taxwitheld'
    ]
    list_editable=['is_payable','is_receivable','bank_activity','is_taxwitheld']

admin.site.register(JournalModel,JournalAdmin)


class PettyCashTransactionAdmin(admin.ModelAdmin):
    search_fields = ['description','amount','received_by']
    list_display = ['date','description','amount','received_by']

admin.site.register(PettyCashTransaction,PettyCashTransactionAdmin)


class PettycashAdmin(admin.ModelAdmin):
    search_fields = ['name','slug','name','amount']
    list_display = ['received_date','name','amount','slug']

admin.site.register(PettycashModel, PettycashAdmin)


admin.site.register(DebtorModel)
admin.site.register(CreditorModel)
admin.site.register(WeeklyProjection)
