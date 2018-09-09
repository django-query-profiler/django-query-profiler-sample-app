from django.db import models

# Create your models here.
class FoodInstance(models.Model):
    class Meta:
        permissions = (
            ("can_order", "Can order the drinks"),
            ("can_serve", "Can prepare and serve the drinks"),
        )
        