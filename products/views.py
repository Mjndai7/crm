from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Product
from .serializers import ProductSerializer
# Create your views here.

class ProductListCreateView(ListCreateAPIView):
    """
    ListCreateAPIView executes both 'GET' and 'POST' requests. i.e listing a queryset or creating a model instance
    """

    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    RetrieveUpdateDestroyAPIView executes 'GET', 'PUT', 'PATCH', & 'DELETE' requests.
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    
