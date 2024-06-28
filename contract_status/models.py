from django.db import models


# Create your models here.
class ContractStatus(models.Model):
    short_description = models.CharField(max_length=350, verbose_name='Краткое содержание', null=True, blank=True)
    contractor = models.CharField(max_length=350, verbose_name='Контрагент')
    contract_name = models.CharField(max_length=350, verbose_name='Договор')
    registration_date = models.DateField(verbose_name='Дата регистрации')
    contract_sum = models.DecimalField(decimal_places=2, max_digits=100,verbose_name='Сумма по договору', null=True, blank=True)
    delivery_deadline = models.DateField(null=True, verbose_name='Крайний срок поставки', blank=True)
    date_receipt = models.DateField(null=True, verbose_name='Дата поступления', blank=True)
    payment_indicator = models.CharField(max_length=100, verbose_name='Признак оплаты', null=True, blank=True)

    date_payment = models.DateField(verbose_name='Дата оплаты', null=True, blank=True)

    supervising_service = models.CharField(max_length=300, verbose_name='Курирующая служба')
    responsible = models.CharField(max_length=600, verbose_name='Ответственный по договору')
    contract_status = models.CharField(max_length=60, verbose_name='Статус договора', null=True, blank=True)
    receipt_warehouse = models.CharField(max_length=100, verbose_name='Склад поступления', null=True, blank=True)
    responsible_warehouse = models.CharField(max_length=200, verbose_name='Ответственный склада', null=True, blank=True)
    type_procurement_item = models.CharField(max_length=50, verbose_name='Вид предмета', null=True, blank=True)


    def __str__(self):
        return f"{self.short_description} - {self.contractor} - {self.contract_name} - {self.registration_date}"

    class Meta:
        verbose_name = 'Статус договоров'
        verbose_name_plural = 'Статус договоров'
