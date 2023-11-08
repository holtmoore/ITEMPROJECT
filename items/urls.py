from django.urls import path
from .views import ItemList, ItemDetail

urlpatterns = [
    path('items/', ItemList.as_view(), name='item_list'),
    path('items/<int:pk>/', ItemDetail.as_view(), name='item_detail')
]

# Compare this snippet from items/serializers.py: