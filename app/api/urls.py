from django.urls import path
from .views import *

urlpatterns = [
    path('card-list/', card_list),
    path('purchases/', purchases),
    path('card/<int:card_id>/detail', card_detail)
]