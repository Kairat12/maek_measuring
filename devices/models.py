from django.db import models

# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=400, verbose_name="Наименование")
    subdivision = models.CharField(max_length=400, verbose_name="Подразделение", null=True, blank=True)
    factory_number = models.CharField(max_length=200,verbose_name="Заводской Номер", null=True, blank=True)
    sensor = models.CharField(max_length=200, verbose_name="Датчик", null=True, blank=True)
    quantity = models.IntegerField(verbose_name="количество", null=True, blank=True)
    date_issued = models.DateField(verbose_name="Дата Выпуска")
    date_entry = models.DateField(verbose_name="Дата Ввода")
    date_verification = models.DateField(verbose_name="Дата Поверки")
    repair_result = models.CharField(max_length=200, verbose_name="Результат Ремонта", null=True, blank=True)
    date_next_verification = models.DateField(verbose_name="Дата Следующей Поверки")
    state = models.CharField(max_length=100, verbose_name="Состояние", null=True, blank=True)
