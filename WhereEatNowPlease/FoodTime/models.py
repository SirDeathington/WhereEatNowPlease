from django.db import models

# Create your models here.
class Account:
    name = models.CharField(max_length=255)

class FoodCatagory:
    name = models.CharField(max_length=255)

class  Restaurant:
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    website = models.URLField(max_length=255)
    #catagories = models.ManyToManyField(FoodCatagory)


