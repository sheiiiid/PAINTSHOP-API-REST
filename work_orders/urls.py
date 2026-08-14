from rest_framework.routers import DefaultRouter
from .views import WorkOrderStatusView, WorkOrderView

router = DefaultRouter()
router.register(r'status', WorkOrderStatusView, basename='status')
router.register(r'work_orders', WorkOrderView, basename='work_orders')

urlpatterns = router.urls