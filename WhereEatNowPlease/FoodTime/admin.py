from django.contrib import admin
from .models import Account, FoodCatagory, Restaurant

# Register your models here.
admin.register(Account)
admin.register(FoodCatagory)
admin.register(Restaurant)