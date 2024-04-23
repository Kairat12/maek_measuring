from django.db import models


class MainSklad(models.Model):
    item_number = models.CharField(max_length=120)
    name = models.CharField(max_length=520,null=True,blank=True)
    unit = models.CharField(max_length=100,null=True,blank=True)
    quantity = models.DecimalField(max_digits=15, decimal_places=2, null=True,blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, null=True,blank=True)
    sum = models.DecimalField(max_digits=15, decimal_places=2, null=True,blank=True)
    date_receipt = models.DateField(null=True,blank=True)
    number_sklad = models.CharField(max_length=400,null=True,blank=True)
    responsible = models.CharField(max_length=100, null=True,blank=True)
    contractor = models.CharField(max_length=300, null=True, blank=True)
    agreement = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return f'{self.item_number}-{self.name}'
