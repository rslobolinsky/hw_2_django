from django.contrib import admin

from catalog.models import Product


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ()
    list_filter = ()
    search_fields = ()
