from django.shortcuts import render
from rest_framework import viewsets
from .models import Inspection
from .serializers import InspectionSerializer

# Create your views here.
class InspectionView(viewsets.ModelViewSet):
    queryset = Inspection.objects.all()
    serializer_class = InspectionSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

