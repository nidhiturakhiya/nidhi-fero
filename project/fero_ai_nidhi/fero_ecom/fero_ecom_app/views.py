from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Product, Order, Customer
from .serializers import ProductSerializer, CustomerSerializer, OrderSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    # @action(detail=False, methods=['get'])
    # def get_orders_by_products(self, request):
    #     # here i am assuming that params will be comma seperated -- We can use any seperator we want and split so
    #     product_names = request.query_params.get('products', '').split(',')
    #     orders = Order.objects.filter(order_item__product__name__in=product_names).distinct()
    #     serializer = self.get_serializer(orders, many=True)
    #     return Response(serializer.data)

    # @action(detail=False, methods=['get'])
    # def get_orders_by_customer(self, request):
    #     customer_name = request.query_params.get('customer', '')
    #     orders = Order.objects.filter(customer__name=customer_name)
    #     serializer = self.get_serializer(orders, many=True)
    #     return Response(serializer.data)