from django.shortcuts import render
from rest_framework import viewsets
from .models import WorkOrderStatus, WorkOrder
from .serializers import WorkOrderStatusSerializer, WorkOrderSerializer

# Create your views here.

class WorkOrderStatusView(viewsets.ModelViewSet):
    queryset = WorkOrderStatus.objects.all()
    serializer_class = WorkOrderStatusSerializer

class WorkOrderView(viewsets.ModelViewSet):
    queryset = WorkOrder.objects.select_related(
        'customer',
        'vehicle',
        'status',
        'user'
    )

    serializer_class = WorkOrderSerializer
