from django.db import models
from django.utils import timezone


# Create your models here.

class Category(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name="subs",
                               verbose_name="والد(اختیاری)")
    title = models.CharField(max_length=255, verbose_name="نام")
    slug = models.SlugField()

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return self.title


class Size(models.Model):
    title = models.CharField(max_length=10, verbose_name="نام")

    class Meta:
        verbose_name = "سایز"
        verbose_name_plural = "سایز های مختلف محصولات"

    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField(max_length=10, verbose_name="نام")

    class Meta:
        verbose_name = "رنگ"
        verbose_name_plural = "رنگ های محصولات"

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ManyToManyField(Category, blank=True, null=True, verbose_name="دسته بندی",
                                      related_name="products")
    title = models.CharField(max_length=30, verbose_name="نام")
    description = models.TextField(verbose_name="توضیحات محصول")
    price = models.IntegerField(verbose_name="قیمت|به تومان")
    discount = models.SmallIntegerField(null=True, blank=True, verbose_name="تخفیف|به درصد")
    image = models.ImageField(upload_to="products", verbose_name="تصویر")
    size = models.ManyToManyField(Size, related_name="products", verbose_name="سایز", null=True, blank=True)
    color = models.ManyToManyField(Color, related_name="products", verbose_name="رنگ")
    created_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def __str__(self):
        return self.title


class Information(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE, related_name="informations",
                                verbose_name="محصول",
                                help_text="محصولی که میخواهید برایش اطلاعات تکمیلی ایجاد کنید را انتخاب کنید")
    text = models.TextField(verbose_name="متن")

    class Meta:
        verbose_name = "اطلاعات تکمیلی"
        verbose_name_plural = "اطلاعات تکمیلی"

    def __str__(self):
        return self.text[:30]


class Offer(models.Model):
    title = models.CharField(max_length=128, verbose_name="عنوان آفر")
    description = models.TextField(verbose_name="توضیحات در مورد آفر")
    discount = models.IntegerField(default=0, verbose_name="تخفیف")
    Image = models.ImageField(null=True, verbose_name="تصویر")
    start_date = models.DateField(default=timezone.now(), verbose_name="زمان شروع")
    end_date = models.DateField(verbose_name="زمان پایان")
    products = models.ManyToManyField(Product, related_name="offers", verbose_name="محصولات")
    is_active = models.BooleanField(default=False, verbose_name="وضعیت آفر",
                                    help_text="این گزینه اگر فعال باشد آفر فعال است و در سایت نمایش داده میشود")

    class Meta:
        verbose_name = "آفر"
        verbose_name_plural = "آفرها"

    def is_active_func(self):
        today = timezone.now().date()
        return self.start_date <= today <= self.end_date

    def __str__(self):
        return self.title
