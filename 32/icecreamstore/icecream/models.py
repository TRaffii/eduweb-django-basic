from django.db import models

# Create your models here.

class Icecream(models.Model):
    name = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=10000)

    def is_really_featured(self):
        if self.is_featured and self.price > 0.00:
            return True
        return False
