# Generated by Django 4.2.11 on 2024-04-22 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainSklad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_number', models.CharField(max_length=120)),
                ('name', models.CharField(blank=True, max_length=520, null=True)),
                ('unit', models.CharField(blank=True, max_length=100, null=True)),
                ('quantity', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('sum', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('date_receipt', models.DateField(blank=True, null=True)),
                ('number_sklad', models.CharField(blank=True, max_length=400, null=True)),
                ('responsible', models.CharField(blank=True, max_length=100, null=True)),
                ('contractor', models.CharField(blank=True, max_length=300, null=True)),
                ('agreement', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
    ]
