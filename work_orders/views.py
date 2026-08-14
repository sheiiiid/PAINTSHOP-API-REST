from django.shortcuts import render
from rest_framework import viewsets
from .models import WorkOrderStatus
from .serializers import WorkOrderStatusSerializer

# Create your views here.

class WorkOrderStatusView(viewsets.ModelViewSet):
    queryset = WorkOrderStatus.objects.all()
    serializer_class = WorkOrderStatusSerializer
s