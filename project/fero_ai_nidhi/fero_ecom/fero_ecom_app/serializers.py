from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from rest_framework import serializers, validators
from .models import Product, Customer, OrderItem, Order
from rest_framework.decorators import action


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        name = serializers.CharField(validators=[validators.UniqueValidator(queryset=Customer.objects.all())])

def validate_positive_decimal(value):
    if value < 0:
        raise ValidationError("Value must be a positive decimal.")

class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[validators.UniqueValidator(queryset=Product.objects.all())])
    weight = serializers.DecimalField(max_digits=5, decimal_places=2, validators=[
        validate_positive_decimal,
        MinValueValidator(0, message="Weight must be a positive decimal."),
        MaxValueValidator(25, message="Weight cannot be more than 25kg.")
    ])
    class Meta:
        model = Product
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    order_number = serializers.CharField(read_only=True)

    class Meta:
        model = Order
        fields = ['order_date', 'address', 'customer', 'order_number']

    def validate_order_date(self, value):
        if value and value < timezone.now().date():
            raise serializers.ValidationError("Order Date cannot be in the past.")
        return value

    @action(detail=False, methods=['get'])
    def get_orders_by_products(self, request):
        product_names = request.query_params.get('products', '').split(',')
        response_data = self.get_serializer().get_orders_by_products(product_names)
        return Response(response_data)

    @action(detail=False, methods=['get'])
    def get_orders_by_customer(self, request):
        customer_name = request.query_params.get('customer', '')
        response_data = self.get_serializer().get_orders_by_customer(customer_name)
        return Response(response_data)
def generate_order_number():
    last_order = Order.objects.order_by('-id').first()
    last_number = last_order.id + 1 if last_order else 1
    return f'ORD{last_number:05d}'