from django.db import models


class Order(models.Model):
    number = models.IntegerField()
    created_date = models.DateTimeField()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    product_price = models.DecimalField(max_digits=2, decimal_places=2)
    amount = models.IntegerField()
