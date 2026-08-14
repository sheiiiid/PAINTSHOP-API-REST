from django.db import models

# Create your models here.
class WorkOrderStatus(models.Model):
    code = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Work_Order_Status'
        verbose_name_plural = 'Work_Order_Status'
        db_table = 'WorkOrderStatus'

class WorkOrder (models.Model):
    customer = models.ForeignKey('customers.Customer', on_delete=models.PROTECT, related_name='work_orders')
    vehicle = models.ForeignKey('vehicles.Vehicle', on_delete=models.PROTECT, related_name='work_orders')
    status = models.ForeignKey('work_orders.WorkOrderStatus', on_delete=models.PROTECT, related_name='work_orders')
    user = models.ForeignKey('users.User', on_delete=models.PROTECT, related_name='work_orders')
    intake_reason = models.CharField(max_length=300)
    initial_observation = models.CharField(max_length=300)
    estimate_cost = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    closed_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.customer

    class Meta:
        verbose_name = 'Work_Order'
        verbose_name_plural = 'Work_Orders'
        db_table = 'WorkOrder'
