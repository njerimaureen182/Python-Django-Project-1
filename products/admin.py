from django.contrib import admin
# to import the Product model:
from .models import Product, Offer
# .model - the models.py module in the current folder
# Product - the Product class in the models.py module

# admin.ModelAdmin is a module imported from (1) above that provides functionality for managing models
# in the admin area
class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


class ProductAdmin(admin.ModelAdmin):
    # list_display is an attribute that specifies the columns that should be visible in our table
    list_display = ('name', 'price', 'stock')


# to manage our products in the admin area:
admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
