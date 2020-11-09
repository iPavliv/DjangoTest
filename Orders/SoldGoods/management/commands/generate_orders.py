import random
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError

from Orders.SoldGoods.models import Order, OrderItem

START_DATE = datetime(2018, 1, 1, 9, 0, 0)


class Command(BaseCommand):
    help = 'Generate certain number of orders.'

    def add_arguments(self, parser):
        parser.add_argument('orders_number', nargs='?', type=int)

    def handle(self, *args, **options):
        orders_number = options['orders_number']

        for order_num in range(orders_number):
            try:
                iter_num = Order.objects.count() + 1

                order_date = START_DATE + timedelta(hours=iter_num)
                new_order = Order.objects.create(number=iter_num, created_date=order_date)
            except IntegrityError:
                raise CommandError('Failed to create new order with number %i.' % iter_num)

            order_items_num = random.randint(1, 5)

            for item in range(order_items_num):
                try:
                    OrderItem.objects.create(
                        order=new_order,
                        product_name=f'Товар-{random.randint(1, 100)}',
                        product_price=round(random.uniform(100, 9999), 2),
                        amount=random.randint(1, 10)
                    )
                except IntegrityError:
                    raise CommandError('Failed to create new order item.')

            self.stdout.write(self.style.SUCCESS('Successfully created %i orders.' % orders_number))
