from rest_framework import serializers
from .models import WorkOrderStatus


class WorkOrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrderStatus
        fields = ['code', 'name']

        read_only_fields = ['code', 'name']

    def create(self, validated_data):
        return WorkOrderStatus.objects.create(**validated_data)