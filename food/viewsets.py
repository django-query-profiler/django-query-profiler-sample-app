from rest_framework import viewsets
from .models import OrderInstance
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = OrderInstance.objects.all()
    serializer_class = OrderSerializer