from django.contrib import admin

from nba_shop.models import Customer, Good, Order

# Register your models here.

admin.site.register(Customer)
admin.site.register(Good)
admin.site.register(Order)