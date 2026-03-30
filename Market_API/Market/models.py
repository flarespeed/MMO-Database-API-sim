from django.db import models

# Create your models here.

class Item(models.Model):
	item_name = models.CharField(max_length=128)
	description = models.CharField(max_length=1280)

class Listing(models.Model):
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	price = models.IntegerField(default=1000)



