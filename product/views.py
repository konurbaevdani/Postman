from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import *
from .models import Product
from .serializer import *
from rest_framework.decorators import APIView

# №1
# -----------------------------------------------------------------------------------


class ProductsListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsListSerializer


class ProductDetailsView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsListSerializer


class CreateProductView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer


class UpdateProductView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer


class DeleteProductView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductsListSerializer
        elif self.action == 'retrieve':
            return ProductDetailsView
        return CreateProductSerializer

# -------------------------------------------------------------------------------------------

#
# @api_view
# def product_list(request):
#     pubs = Product.object.all()
#     serializer = ProductsListSerializer(pubs, many=True)
#     return Response(serializer.data)


