import random
import datetime
import pytz
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Generates data for simple sales app'

    def add_arguments(self, parser):
        parser.add_argument('--clients', type=int, action='store', help='Number of client to get generated, default 10')
        parser.add_argument('--product', type=int, action='store',
                            help='Number of products t0o get generated, default 10')
        parser.add_argument('--expenses', type=int, action='store',
                            help='Number of Expense to get generated, default 10')

        parser.add_argument('--expense-transaction', type=int, action='store',
                            help='Number of records per day,  default 10')

    def handle(self, *args, **options):
        from ...models import Client, Product, SalesTransaction, SalesLineTransaction, Expense, ExpenseTransaction
        from django.contrib.auth.models import User
        user_id = User.objects.first().pk
        client_count = options.get('clients', 10) or 10
        product_count = options.get('products', 10) or 10
        records_per_day = options.get('records', 10) or 10

        expense_count = options.get('expenses', 10) or 10
        etransaction_per_day = options.get('expense-transaction', 3) or 3

        # Generating clients
        already_recorded = Client.objects.all().count()
        clients_needed = client_count - already_recorded
        if clients_needed > 0:
            for index in range(already_recorded, already_recorded + clients_needed):
                Client.objects.create(name=f'Client {index}', slug=index)
            self.stdout.write(f'{clients_needed} client(s) created')

        # Product
        already_recorded = Product.objects.all().count()
        product_needed = product_count - already_recorded
        if product_needed > 0:
            for index in range(already_recorded, already_recorded + product_needed):
                Product.objects.create(name=f'Product {index}', slug=index)
            self.stdout.write(f'{product_needed} product(s) created')

        already_recorded = Expense.objects.all().count()
        Expenses_needed = expense_count - already_recorded
        if Expenses_needed > 0:
            for index in range(already_recorded, already_recorded + Expenses_needed):
                Expense.objects.create(name=f'Expense {index}', slug=index)
            self.stdout.write(f'{Expenses_needed} Expense(s) created')

        # generating sales
        # we will generate 10 records per day for teh whole current year
        sdate = datetime.datetime(datetime.date.today().year, 1, 1)
        edate = datetime.datetime(datetime.date.today().year, 12, 31)

        client_ids = Client.objects.values_list('pk', flat=True)
        product_ids = Product.objects.values_list('pk', flat=True)
        expense_ids = Expense.objects.values_list('pk', flat=True)

        delta = edate - sdate  # as timedelta
        for i in range(delta.days + 1):
            day = sdate + datetime.timedelta(days=i)
            day = pytz.utc.localize(day)
            for z in range(1, records_per_day):
                chosen_client = random.choice(client_ids)
                SalesLineTransaction.objects.create(
                    transaction_date=day,
                    # sales_transaction=SalesTransaction.objects.create(transaction_date=day, client_id=chosen_client),
                    product_id=random.choice(product_ids),
                    client_id=chosen_client,
                    quantity=random.randrange(1, 10),
                    price=random.randrange(1, 10),
                    # doc_type = 'sales'
                )

            for z in range(1, etransaction_per_day):
                ExpenseTransaction.objects.create(
                    transaction_date=day,
                    expense_id=random.choice(expense_ids),
                    value=random.randrange(1, 10)
                )
            self.stdout.write(f'{day} Done')
            self.stdout.flush()

        self.stdout.write('----')
        self.stdout.write('Done')
