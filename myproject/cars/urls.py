from django.urls import path,include
from .views import *


urlpatterns = [
    path('', CarsViewSet.as_view({'get': 'list', 'post': 'create'}),
                                                 name='marka_list'),
    path('<int:pk>/', CarsViewSet.as_view({'get': 'retrieve',
        'put': 'update', 'delete': 'destroy'}), name='product_detail'),


    path('category', ModelViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='model_list'),
    path('accounts/', include('allauth.urls')),
    path('category/<int:pk>/', ModelViewSet.as_view({'get': 'retrieve',
    'put': 'update', 'delete ': 'destroy'}), name='category_detail'),


    path('category', MarkaViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='category_list'),
    path('accounts/', include('allauth.urls')),
    path('category/<int:pk>/', MarkaViewSet.as_view({'get': 'retrieve',
    'put': 'update', 'delete ': 'destroy'}), name='cars_detail')

]