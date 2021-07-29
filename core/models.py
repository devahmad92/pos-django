from django.db import models

class Order(models.Model):
    name = models.CharField(max_length=200)
    order_id = models.PositiveBigIntegerField()
    order_status = models.BooleanField()

    user_id = models.PositiveIntegerField()

    restaurant_id = models.PositiveIntegerField()

    device_token = models.CharField(max_length=200)

    user_lat = models.DecimalField(max_digits=9, decimal_places=6)
    user_lng = models.DecimalField(max_digits=9, decimal_places=6)

    restaurant_lat = models.DecimalField(max_digits=9, decimal_places=6)
    restaurant_lng = models.DecimalField(max_digits=9, decimal_places=6)

    food_id = models.PositiveIntegerField()

    user_notes = models.TextField()

    driver_id = models.PositiveIntegerField()


    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
