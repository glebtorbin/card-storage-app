from rest_framework.decorators import api_view
from rest_framework import status, filters
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.utils import timezone

import datetime

from .utils import generator
from storage.models import Card, Payment
from .serializers import CardSerializer, CardDetailSerializer, PaymentSerializer


class CardListView(ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['series', 'number', 'release_date', 'ending_date', 'status']

@api_view(['GET'])
def card_detail(request, card_id):
    '''Фунуция возвращает детальную информацию о карте со списком транзакций'''
    try:
        card = Card.objects.get(id=card_id)
        serializer = CardDetailSerializer(card, many=False)
        return Response({'card': serializer.data})
    except Card.DoesNotExist:
        return Response(
            {'message': 'карты с таким id не существует'},
            status=status.HTTP_404_NOT_FOUND
        )


@api_view(['GET'])
def purchases(request):
    """Функция выводит весь список покупок по всем картам"""
    payments = Payment.objects.all()
    serializer = PaymentSerializer(payments, many=True)
    return Response({'purchases': serializer.data})

@api_view(['GET'])
def card_activation(request, card_id):
    '''функция активирования карты'''
    try:
        card = Card.objects.get(id=card_id)
        if card.status == 'ACTIVE' or card.status == 'Active':
            return Response(
                {'message': 'Ваша карта уже активирована'},
                status=status.HTTP_200_OK
            )
        elif card.status == 'OVERDUE' or card.status == 'Overdue':
            return Response(
                {'message': 'Ваша карта просрочена, обратитесь к менеджеру'},
                status=status.HTTP_200_OK
            )
        card.status = 'ACTIVE'
        card.save()
        return Response(
            {'message': f'Ваша карта {card.series}{card.number} активирована! Позравляем!'},
            status=status.HTTP_200_OK
        )
    except Card.DoesNotExist:
        return Response(
            {'message': 'карты с таким id не существует'},
            status=status.HTTP_404_NOT_FOUND
        )

# мы можем также выбрать метод 'DELETE',
# но на мой взгляд - пользователю будет удобнее отправлять GET запрос
@api_view(['GET'])
def card_delete(request, card_id):
    '''функция удаляет карту из базы данных'''
    try:
        Card.objects.get(id=card_id).delete()
        return Response(
            {'message': 'Ваша карта удалена!'},
            status=status.HTTP_204_NO_CONTENT
        )
    except Card.DoesNotExist:
        return Response(
            {'message': 'карты с таким id не существует'},
            status=status.HTTP_404_NOT_FOUND
        )
@api_view(['GET'])
def card_generator(request, series: int, number: int, term: str):
    '''Функция реализует генератор карт'''
    try:
        if term == '1year':
            ending_date = datetime.datetime.now() + datetime.timedelta(weeks=52, days=1)
        elif term == '6month':
            ending_date = datetime.datetime.now() + datetime.timedelta(weeks=26, hours=12)
        elif term == '1month':
            ending_date = datetime.datetime.now() + datetime.timedelta(days=31)
        else:
            return Response(
                {'message': 'Варианты срока карты: <1year>, <6month>, <1month>'},
                status=status.HTTP_200_OK
            )
        for i in range(number+1):
            Card.objects.create(
                series=series,
                number=generator(),
                ending_date=ending_date
            )
        if number == 1:
            return Response(
                {'message': '1 карта успешно созданы'},
                status=status.HTTP_201_CREATED
                )
        elif number == (2 or 3 or 4):
            return Response(
                {'message': f'{number} карты успешно созданы'},
                status=status.HTTP_201_CREATED
                )
        else:
            return Response(
                {'message': f'{number} карт успешно созданы'},
                status=status.HTTP_201_CREATED
                )
    except:
        return Response(
            {'message': 'Что-то пошло не так, попробуйте позже'},
            status=status.HTTP_503_SERVICE_UNAVAILABLE
        )

@api_view(['GET'])
def update_status(request):
    '''Функция проверяет и изменяет статусы карт'''
    try:
        cards = Card.objects.all()
        for card in cards:
            if card.ending_date <= timezone.now():
                print(card.ending_date, timezone.now())
                card.status = 'OVERDUE'
                card.save()
        return Response({'message': 'Данные обновлены!'},
                        status=status.HTTP_200_OK)
    except Exception as error:
        return Response(
            {'message': f'{error}'},
            status=status.HTTP_503_SERVICE_UNAVAILABLE
        )