from django.urls import path

from .views import ProductViewSet, UserAPIView, add_to_cart

urlpatterns = [
    path('products', ProductViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('products/<str:pk>', ProductViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('products/<str:pk>', ProductViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('products/<str:pk>/add', add_to_cart, name='add_to_cart'),
    path('user', UserAPIView.as_view())
]