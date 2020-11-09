from django.db import models


class Order(models.Model):
    number = models.IntegerField()
    created_date = models.DateTimeField()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    product_price = models.DecimalField(max_digits=15, decimal_places=5)
    amount = models.IntegerField()
