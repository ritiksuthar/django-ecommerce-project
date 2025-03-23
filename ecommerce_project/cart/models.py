from django.db import models
from django.contrib.auth.models import User
from product.models import Product
from django.conf import settings 

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    print(user)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    print(product)
    quantity = models.IntegerField(default=1)
    print(quantity)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.total_price = (self.product.price or  0) * (self.quantity or 0 )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
    

