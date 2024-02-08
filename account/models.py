from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from account.managers import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="آدرس ایمیل",
        max_length=255,
        null=True,
        blank=True,
        unique=True,
    )
    fullname = models.CharField(max_length=60, verbose_name="نام کامل")
    phone = models.CharField(max_length=12, unique=True, verbose_name="شماره تلفن همراه")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False, verbose_name="ادمین")

    objects = UserManager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربرها"

    def __str__(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Otp(models.Model):
    token = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=11)
    code = models.SmallIntegerField()
    expiration_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "اعتبارسنجی"
        verbose_name_plural = "اعتبارسنجی ها"

    def __str__(self):
        return self.phone


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="addresses", verbose_name="کاربر")
    fullname = models.CharField(max_length=60, verbose_name="نام کامل")
    email = models.EmailField(null=True, blank=True, verbose_name="ایمیل")
    phone = models.CharField(max_length=12, verbose_name="شماره تلفن")
    address = models.CharField(max_length=255, verbose_name="آدرس")
    postal_code = models.CharField(max_length=30, verbose_name="کد پستی")

    class Meta:
        verbose_name = "آدرس"
        verbose_name_plural = "آدرس ها"

    def __str__(self):
        return self.user.phone
