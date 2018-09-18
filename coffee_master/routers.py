from rest_framework import routers
from food.viewsets import OrderViewSet

router = routers.DefaultRouter()
router.register(r'order', OrderViewSet)
