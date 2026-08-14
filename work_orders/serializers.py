from rest_framework import serializers
from .models import WorkOrderStatus, WorkOrder


class WorkOrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrderStatus
        fields = ['code', 'name']

        read_only_fields = ['code', 'name']

    def create(self, validated_data):
        return WorkOrderStatus.objects.create(**validated_data)

class WorkOrder(serializers.ModelSerializer):
    class Meta:
        model = WorkOrder
        fields = '__all__'

        read_only_fields = ['id', 'created_at', 'updated_at']