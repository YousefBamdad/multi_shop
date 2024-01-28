from django.contrib import admin
from product import models


# Register your models here.

class InformationAdmin(admin.StackedInline):
    model = models.Information

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "price"]
    inlines = [InformationAdmin, ]


# admin.site.register(models.Product)
admin.site.register(models.Size)
admin.site.register(models.Color)
