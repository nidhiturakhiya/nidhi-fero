from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2)

class Order(models.Model):
    ORDER_NUMBER_PREFIX = 'ORD'
    
    order_number = models.CharField(max_length=10, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField()
    address = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        # Auto-generate order number with the prefix 'ORD' and 5-digit numbers
        if not self.order_number:
            last_order = Order.objects.order_by('-id').first()
            last_number = last_order.id + 1 if last_order else 1
            self.order_number = f'{self.ORDER_NUMBER_PREFIX}{last_number:05d}'
        super(Order, self).save(*args, **kwargs)
        
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
