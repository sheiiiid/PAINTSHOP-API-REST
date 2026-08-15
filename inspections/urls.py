from rest_framework import routers
from .views import InspectionView

router = routers.DefaultRouter()
router.register(r'inspections', InspectionView, basename='inspections')

urlpatterns = router.urls