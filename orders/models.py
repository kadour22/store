from django.db import models
from products.models import Product

class Order(models.Model) :

    class ORDER_CHOICES (models.TextChoices) :
        PENDING  = "pending","pending"
        DECLINED = "declined","declined"
        PASSED   = "passed","passed"
    
    status = models.CharField(max_length = 20 ,
    choices = ORDER_CHOICES.choices,
    default = ORDER_CHOICES.PENDING
    )
    total_price = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    created_at  = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model) :
    order    = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product  = models.ForeignKey(Product, on_delete=models.CASCADE, related_name = "order_items")
    quantity = models.IntegerField() 
    created  = models.DateTimeField(auto_now_add = True)