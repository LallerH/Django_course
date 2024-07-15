import csv
from django.core.management import BaseCommand
from django.core.management.base import CommandParser
from ... models import Product

class Command(BaseCommand):
    help = 'Import products from csv file'
    
    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Input csv file')
    
    def handle(self, *args, **options):
        print('Import Products..')
        # file_path = 'products.csv'
        file_path = options['csv_file']
        try:
            with open(file_path, encoding='utf-8') as f:
                # print(f.read())
                reader = csv.DictReader(f)
                for row in reader:
                    print(row)
                    try:
                        Product.objects.create(
                            product_name=row['name'],
                            product_price=row['price']
                            )
                    except Exception as e:
                        print(self.style.WARNING(f'Error: {e}, row {row} skipped!'))
                print(Product.objects.all())
                print(self.style.SUCCESS(f'{file_path} succesfully imported.'))

        except FileNotFoundError:
            print(self.style.ERROR(f'{file_path} does not exists.'))