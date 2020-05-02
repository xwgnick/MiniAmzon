from django.urls import path

from .views import *

urlpatterns = [
    path('', search_item, name='home'),
    path('signup/', signup, name='signup'),
    path('<str:product_name>/Add', add_to_cart, name='addToCart'),
    path('myCart/', check_my_cart.as_view(), name='mycart'),
    path('myOrders/', view_my_order.as_view(), name='myorders'),
    path('<str:pk>/delete/', CartDeleteView.as_view(), name = 'cart-delete'),
    path('<str:pk>/update/', CartUpdateView.as_view(), name = 'cart-update'),
    path('myCart/placeorder/', place_order, name='placemyorder'),
]