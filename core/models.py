from django.db import models

class Order(models.Model):
    name = models.CharField(max_length=200)
    order_id = models.PositiveBigIntegerField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)