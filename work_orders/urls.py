from rest_framework.routers import DefaultRouter
from .views import WorkOrderStatusView, WorkOrderView, WorkOrderStatusHistoryView

router = DefaultRouter()
router.register(r'status', WorkOrderStatusView, basename='status')
router.register(r'work_orders', WorkOrderView, basename='work_orders'),
router.register(r'status_history', WorkOrderStatusHistoryView, basename='status_history'),

urlpatterns = router.urls