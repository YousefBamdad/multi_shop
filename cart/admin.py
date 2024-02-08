from django.contrib import admin
from cart import models


# Register your models here.


class OrderItemInline(admin.TabularInline):
    model = models.OrderItem


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_paid']
    inlines = [OrderItemInline]
    list_filter = ['is_paid']


@admin.register(models.DiscountCode)
class DiscountCodeAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'discount']
