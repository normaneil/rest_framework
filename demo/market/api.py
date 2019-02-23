from market.models import Users, Orders
from django.db.models import Q
from rest_framework import viewsets, permissions
from .serializers import UsersSerializer, OrdersSerializer, GetOrdersSerializer

from rest_framework.filters import (
  SearchFilter,
  OrderingFilter
)

class UsersViewSet(viewsets.ModelViewSet):
  queryset = Users.objects.all()
  permission_classes = [
    permissions.AllowAny
  ]
  serializer_class = UsersSerializer

class OrdersViewSet(viewsets.ModelViewSet):
  queryset = Orders.objects.all()
  permission_classes = [
    permissions.AllowAny
  ]
  serializer_class = OrdersSerializer

# Working
class GetOrdersViewSet(viewsets.ModelViewSet):
  serializer_class = GetOrdersSerializer
  # queryset = Users.objects.all()
  permission_classes = [
    permissions.AllowAny
  ]
  filter_backends = [SearchFilter]
  search_fields = ['user_first_name', 'user_last_name']
  

  def get_queryset(self, *args, **kwargs):
    queryset = Users.objects.all()
    query = self.request.GET.get("q")
    print(query)
    if query:
      queryset = queryset.filter(
        Q(user_first_name__icontains = query) |
        Q(user_last_name__icontains = query)
      ).distinct()
      return queryset
    return queryset

