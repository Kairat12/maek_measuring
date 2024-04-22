import os
from django.core.management.base import BaseCommand
from sklad.models import MainSklad  # Замените на вашу модель
from openpyxl import load_workbook
from datetime import datetime

class Command(BaseCommand):
    help = 'Import data from Excel'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to Excel file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR('File does not exist'))
            return

        try:
            workbook = load_workbook(file_path)
            sheet = workbook.active

            for index, row in enumerate(sheet.iter_rows(values_only=True)):
                if index < 4:
                    continue

                sklad, created = MainSklad.objects.get_or_create(
                    item_number=row[0],
                    name=row[1],
                    defaults={'unit': row[2],
                              'quantity': row[3],
                              'price': row[4],
                              'sum': row[5],
                              'date_receipt': datetime.strptime(row[6], '%d.%m.%y').strftime('%Y-%m-%d'),
                              'number_sklad': row[7],
                              'responsible': row[8],
                              'contractor': row[9],
                              'agreement': row[10],
                              }
                )
                if created:
                    self.stdout.write(f"Создана запись: {sklad}")
                else:
                    sklad.item_number = row[0]
                    sklad.name = row[1]
                    sklad.unit = row[2]
                    sklad.quantity = row[3]
                    sklad.price = row[4]
                    sklad.sum = row[5]
                    sklad.date_receipt = datetime.strptime(row[6], '%d.%m.%y').strftime('%Y-%m-%d') if row[6] != '' else datetime.strptime('1970-01-01', '%d.%m.%y').strftime('%Y-%m-%d')
                    sklad.number_sklad = row[7]
                    sklad.responsible = row[8]
                    sklad.contractor = row[9] if row[6] != '' else ''
                    sklad.agreement = row[10] if row[6] != '' else ''
                    sklad.save()
                    self.stdout.write(f"Обновлена запись: {sklad}")

            # self.stdout.write(self.style.SUCCESS('Data imported successfully'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {e}'))
