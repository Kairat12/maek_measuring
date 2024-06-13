from django.db import models


# Create your models here.
class ContractStatus(models.Model):
    short_description = models.CharField(max_length=350, verbose_name='Краткое содержание')
    contractor = models.CharField(max_length=350, verbose_name='Контрагент')
    contract_name = models.CharField(max_length=350, verbose_name='Договор')
    registration_date = models.DateField(verbose_name='Дата регистрации')
    contract_sum = models.DecimalField(decimal_places=3, max_digits=100,verbose_name='Сумма по договору')
    delivery_deadline = models.DateField(null=True, verbose_name='Крайний срок поставки')
    date_receipt = models.DateField(null=True, verbose_name='Дата поступления')
    payment_indicator = models.CharField(max_length=100, verbose_name='Признак оплаты')
    supervising_service = models.CharField(max_length=300, verbose_name='Курирующая служба')
    responsible = models.CharField(max_length=600, verbose_name='Ответственный по договору')
    contract_status = models.CharField(max_length=60, verbose_name='Статус договора')
    receipt_warehouse = models.CharField(max_length=100, verbose_name='Склад поступления')
    responsible_warehouse = models.CharField(max_length=200, verbose_name='Ответственный склада')

    def __str__(self):
        return f"{self.short_description} - {self.contractor} - {self.contract_name} - {self.registration_date}"

    class Meta:
        verbose_name = 'Статус договоров'
