from django.contrib import admin
from .models import Account, FoodCatagory, Restaurant

# Register your models here.
admin.site.register(Account)
admin.site.register(FoodCatagory)
admin.site.register(Restaurant)