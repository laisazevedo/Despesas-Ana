from django.contrib import admin
from .models import Despesas_Ana

class DespesaAdmin(admin.ModelAdmin):
    list_display =  ('vencimento','descrição','quitado','Forma_Pagamento')
admin.site.register(Despesas_Ana, DespesaAdmin)
