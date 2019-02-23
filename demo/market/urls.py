from rest_framework import routers
from .api import UsersViewSet, OrdersViewSet, GetOrdersViewSet

router = routers.DefaultRouter()
router.register('api/users', UsersViewSet, 'users')
router.register('api/orders', OrdersViewSet, 'orders')
router.register('api/order-list', GetOrdersViewSet, 'order-list')

urlpatterns =router.urls