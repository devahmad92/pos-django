from rest_framework import generics
from .serializers import OrderSerializer
from ..models import Order

class OrderListCreateApiView(generics.ListAPIView, generics.CreateAPIView):
    model = Order
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetailUpdateDeleteApiView(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    model = Order
    queryset = Order.objects.all()
    serializer_class = OrderSerializer