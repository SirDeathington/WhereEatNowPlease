from django.db import models

# Create your models here.


class Account(models.Model):
    name = models.CharField(max_length=255)


class FoodCatagory(models.Model):
    name = models.CharField(max_length=255)


class  Restaurant(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    website = models.URLField(max_length=255)
    #catagories = models.ManyToManyField(FoodCatagory)


