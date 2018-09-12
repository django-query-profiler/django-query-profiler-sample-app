from django.db import models

# Create your models here.
class FoodInstance(models.Model):
    class Meta:
        permissions = (
            ("can_order", "Can order the drinks"),
            ("can_serve", "Can prepare and serve the drinks"),
        )

class OrderInstance(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    coffee_order = models.CharField(max_length=100)