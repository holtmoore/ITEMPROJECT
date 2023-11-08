from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    quantity = models.IntegerField()
    rarity = models.CharField(max_length=100)

    def __str__(self):
        return self.name


