from rest_framework import routers
from core import viewsets

router = routers.DefaultRouter()

router.register(r'category', viewsets.CategoryViewSet)
router.register(r'dvd', viewsets.DvdViewSet)
router.register(r'rental_item', viewsets.RentalItemViewSet)
router.register(r'rental', viewsets.RentalViewSet)
router.register(r'employee', viewsets.EmployeeViewSet)
router.register(r'customer', viewsets.CustomerViewSet)

urlpatterns = router.urls
