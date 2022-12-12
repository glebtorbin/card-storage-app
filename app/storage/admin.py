from django.contrib import admin

from .models import Card, Payment


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('purchase_amount', 'purchase_date')
    

class CardAdmin(admin.ModelAdmin):
    list_display = ('series', 'number', 'release_date', 'ending_date', 'status')
    list_editable = ('status',)
    search_fields = ('number',)
    list_filter = ('release_date',)
    empty_value_display = '-пусто-'


admin.site.register(Card, CardAdmin)
admin.site.register(Payment, PaymentAdmin)
