from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_amount','order_status', 'created_at', 'updated_at')
    list_filter = ('order_status',)



