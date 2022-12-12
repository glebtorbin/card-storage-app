from datetime import date

from rest_framework import serializers

from storage.models import Card, Payment


class PaymentSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = '__all__'
        model = Payment

class CardDetailSerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(many=True, read_only=True)

    class Meta:
        fields = ('id', 'series', 'number', 'release_date', 'ending_date', 'status', 'payments')
        model = Card


class CardSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ('id', 'series', 'number', 'release_date', 'ending_date', 'status')
        read_only_fields = ('release_date', )
        model = Card

    # def validate_done_date(self, data):
    #     now = date.today()
    #     if now > data:
    #         raise serializers.ValidationError(
    #             f"Вы не можете указать дату меньше чем {now}"
    #         )
    #     return data

    # def validate_title(self, title):
    #     obj = Task.objects.filter(title=title, done='False')
    #     if obj:
    #         raise serializers.ValidationError(
    #             "Вы указали задание с существующим названием"
    #         )
    #     return title