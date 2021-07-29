from rest_framework.serializers import ModelSerializer
from ..models import  Order


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class OrderDetailSerializer(ModelSerializer):
    class Meta:
        model = Order
        exclude = ["order_status", "created", "updated", "driver_id"]
