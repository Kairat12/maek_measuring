from django.db import models


class MainSklad(models.Model):
    item_number = models.CharField(max_length=120, verbose_name="Номенклатурный номер")
    name = models.CharField(max_length=520,null=True,blank=True, verbose_name="Наименование")
    unit = models.CharField(max_length=100,null=True,blank=True, verbose_name="Единица измерения")
    quantity = models.DecimalField(max_digits=15, decimal_places=3, null=True,blank=True, verbose_name="Количество")
    price = models.DecimalField(max_digits=15, decimal_places=3, null=True,blank=True, verbose_name="Цена")
    sum = models.DecimalField(max_digits=15, decimal_places=3, null=True,blank=True, verbose_name="Сумма")
    date_receipt = models.DateField(null=True,blank=True, verbose_name="Дата поступления")
    number_sklad = models.CharField(max_length=400,null=True,blank=True, verbose_name="№ склада")
    responsible = models.CharField(max_length=100, null=True,blank=True, verbose_name="Ответственный")
    contractor = models.CharField(max_length=300, null=True, blank=True, verbose_name="Контрагент")
    agreement = models.CharField(max_length=300, null=True, blank=True, verbose_name="Договор")

    def __str__(self):
        return f'{self.item_number}-{self.name}'
