from django.db import models

from account.models import User
from product.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders", verbose_name="کاربر")
    total_price = models.IntegerField(default=0, verbose_name="قیمت کل")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="ایجاد شده در")
    is_paid = models.BooleanField(default=False, verbose_name="پرداخت شده")

    class Meta:
        verbose_name = "سفارش"
        verbose_name_plural = "سفارشات"

    def __str__(self):
        return self.user.phone


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items", verbose_name="سفارش")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="items", verbose_name="محصول")
    size = models.CharField(max_length=12, verbose_name="سایز", blank=True, null=True)
    color = models.CharField(max_length=12, verbose_name="رنگ")
    quantity = models.SmallIntegerField(verbose_name="تعداد")
    price = models.PositiveIntegerField(verbose_name="قیمت")

    class Meta:
        verbose_name = "جزییات سفارش"
        verbose_name_plural = "جزییات سفارشات (محصولات سفارشات)"


    def __str__(self):
        return self.order.user.phone


class DiscountCode(models.Model):
    name = models.CharField(max_length=30, verbose_name="عنوان و کد تخفیف", unique=True)
    discount = models.SmallIntegerField(default=0, verbose_name="درصد تخفیف")
    quantity = models.SmallIntegerField(default=1, verbose_name="تعداد موجود")


    class Meta:
        verbose_name = "کد تخفیف"
        verbose_name_plural = "کدهای تخفیف"

    def __str__(self):
        return self.name
