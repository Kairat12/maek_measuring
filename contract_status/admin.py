from django.contrib import admin

from contract_status.models import ContractStatus

# Register your models here.

class ContractStatusAdmin(admin.ModelAdmin):
    search_fields = ['short_description']

admin.site.register(ContractStatusAdmin,ContractStatus)