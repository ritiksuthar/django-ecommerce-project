from django.db import models
from django.conf import settings

ORDER_STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Confirmed', 'Confirmed'),
    ('Shipped', 'Shipped'),
    ('Delivered', 'Delivered'),
    ('Canceled', 'Canceled'),
]

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  
    cart = models.ManyToManyField('cart.Cart', related_name="orders")  # Related name added
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)  # More precise for money values
    payment_id = models.CharField(max_length=100, blank=True, null=True)  # Razorpay Payment ID
    order_status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']  # Orders will be sorted by most recent first
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"Order #{self.id} - {self.user.username} - {self.order_status}"
