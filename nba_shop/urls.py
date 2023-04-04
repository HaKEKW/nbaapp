from django.urls import path
from .views import *


urlpatterns = [
    path('', view, name='shop_url'),

    path('admin/panel/', AdminPanelView.as_view(), name='admin_panel_url'),
    path('admin/products/', GoodView.as_view(), name='goods_url'),
    path('admin/products/create/', GoodCreateView.as_view(), name='good_create_url'),
    path('admin/products/delete/<str:pk>/', GoodDeleteView.as_view(), name='good_delete_url'),
    path('admin/products/update/<str:pk>/', GoodUpdateView.as_view(), name='good_update_url'),

    path('admin/order/update/<str:pk>/', OrderUpdateView.as_view(), name='order_update_url'),
    path('admin/order/delete/<str:pk>/', OrderDeleteView.as_view(), name='order_delete_url'),
    path('admin/customer-info/<str:pk>/', CustomerPanelView.as_view(), name='customer_info_url'),

    path('<str:pk>/', GoodDetailView.as_view(), name='good_detail_url'),

]

