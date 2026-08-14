from rest_framework import routers
from .views import VehicleView

router = routers.DefaultRouter()
router.register(r'vehicles', VehicleView, basename='vehicles')

urlpatterns = router.urls