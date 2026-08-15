from django.shortcuts import render
from rest_framework import viewsets
from .models import WorkOrderStatus, WorkOrder, WorkOrderStatusHistory
from .serializers import WorkOrderStatusSerializer, WorkOrderSerializer, WorkOrderStatusHistorySerializer

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

class WorkOrderStatusHistoryView(viewsets.ModelViewSet):
    queryset = WorkOrderStatusHistory.objects.select_related(
        'work_order',
        'previous_status',
        'new_status',
        'user',
    )

    serializer_class = WorkOrderStatusHistorySerializer