from django.urls import path
from .views import *

# ---------------------------------------------------------------------

# urlpatterns = [
#     path('products/', ProductViewSet.as_view(
#         {'get': 'list',
#          'post': 'create'}
#     )),
#     path('products/<int:pk>/', ProductViewSet.as_view(
#         {'get': 'retrieve',
#          'put': 'update',
#          'patch': 'partial_update',
#          'delete': 'destroy'}
#     )),
# ]
# -------------------------------------------------------------------


urlpatterns = [
    path('products/', ProductViewSet.as_view(
        {'get': 'list'}
    )),
    path('products/<int:pk>/', ProductViewSet.as_view(
        {'get': 'retrieve'}
    )),
    path('products/create/', ProductViewSet.as_view(
        {'post': 'create'}
    )),
    path('products/update/<int:pk>/', ProductViewSet.as_view(
        {'put': 'update', 'patch': 'partial_update'}
    )),
    path('products/delete/<int:pk>/', ProductViewSet.as_view(
        {'delete': 'destroy'}
    ))
]

# --------------------------------------------------------------------------------------


# urlpatterns = [
#     path('products/', ProductsListView.as_view()),
#     path('products/<int:pk>/', ProductDetailsView.as_view()),
#     path('products/create/', CreateProductView.as_view()),
#     path('products/update/<int:pk>/', UpdateProductView.as_view()),
#     path('products/delete/<int:pk>/', DeleteProductView.as_view())
# ]
