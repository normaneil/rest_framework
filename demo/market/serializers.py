from rest_framework import serializers
from market.models import Orders, Users

class UsersSerializer(serializers.ModelSerializer):
  class Meta:
    model = Users
    fields = '__all__'

class OrdersSerializer(serializers.ModelSerializer):
  class Meta:
    model = Orders
    fields = '__all__'

class GetOrdersSerializer(serializers.ModelSerializer):
    orders = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='order_name'
     )
    class Meta:
        model = Users
        fields = ('user_first_name', 'user_last_name', 'orders')
