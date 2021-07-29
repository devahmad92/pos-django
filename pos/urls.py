from django.contrib import admin
from django.urls import path, include
from core.api.views import OrderListCreateApiView, OrderDetailUpdateDeleteApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/orders', OrderListCreateApiView.as_view(), name="orders-list-create"),
    path('api/v1/orders/<int:pk>', OrderDetailUpdateDeleteApiView.as_view(), name="orders-detail-update-delete")



]
