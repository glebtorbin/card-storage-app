from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from storage.models import Card, Payment
from .serializers import CardSerializer, CardDetailSerializer, PaymentSerializer


@api_view(['GET'])
def card_list(request):
    """Функция выводит весь список карт"""
    cards = Card.objects.all()
    serializer = CardSerializer(cards, many=True)
    return Response({'cards': serializer.data})

@api_view(['GET'])
def card_detail(request, card_id):
    '''Фунуция возвращает детальную информацию о карте со списком транзакций'''
    card = Card.objects.get(id=card_id)
    serializer = CardDetailSerializer(card, many=False)
    return Response({'card': serializer.data})

@api_view(['GET'])
def purchases(request):
    """Функция выводит весь список покупок по всем картам"""
    payments = Payment.objects.all()
    serializer = PaymentSerializer(payments, many=True)
    return Response({'purchases': serializer.data})