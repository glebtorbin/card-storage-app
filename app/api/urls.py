from django.urls import path
from .views import *

urlpatterns = [
    path('card-list/', CardListView.as_view()),
    path('purchases/', purchases),
    path('card/<int:card_id>/detail', card_detail),
    path('card/<int:card_id>/activate', card_activation),
    path('card/<int:card_id>/delete', card_delete),
    path('card/generate/<int:series>/<int:number>/<str:term>', card_generator),
    path('update-status/', update_status),
]