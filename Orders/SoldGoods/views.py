from django.db.models import Sum, F, DecimalField, Count
from django.http import HttpResponse
from django.views import View

from SoldGoods.models import Order, OrderItem


class OrdersByPeriodView(View):
    def get(self, request):
        max_date = request.GET.get('max_date', '9999-12-31')
        min_date = request.GET.get('min_date', '2018-01-01')
        orders_by_time = list(
            Order.objects.filter(created_date__lte=max_date).filter(created_date__gte=min_date)
            .order_by('-created_date'))
        result = []

        for order in orders_by_time:
            order_items = list(
                OrderItem.objects
                    .filter(order__id=order.id)
                    .values('product_name', 'product_price', 'amount')
                    .annotate(price=Sum(F('product_price') * F('amount'), output_field=DecimalField())))
            order_sum = sum((x['price'] for x in order_items))
            result.append({
                'created_date': order.created_date,
                'number': order.number,
                'total_price': order_sum,
                'goods': order_items,
            })

        return HttpResponse(result)


class MostPurchasedView(View):
    def get(self, request):
        max_date = request.GET.get('max_date', '9999-12-31')
        min_date = request.GET.get('min_date', '2018-01-01')

        order_items = list(OrderItem.objects
            .filter(order__created_date__lte=max_date).filter(order__created_date__gte=min_date)
            .values('product_name')
            .annotate(most_purchased=Count(F('product_name')))
            .order_by('-most_purchased'))[:20]
        result = []

        for item in order_items:
            item_orders = list(
                OrderItem.objects
                    .filter(product_name=item['product_name'])
                    .values('order__number', 'product_price', 'order__created_date')
                    .order_by('-order__created_date'))
            result.append({'product_name': item['product_name'], 'orders': item_orders})

        return HttpResponse(result)
