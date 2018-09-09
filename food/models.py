from django.db import models

# Create your models here.
class FoodInstance(models.Model):
    class Meta:
        permissions = (
            ("can_order", "Can order the drink"),
            ("can_server", "Can prepare and serve the drink"),
        )