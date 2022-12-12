from django.db import models

ACT = 'ACTIVE'
DEACT = 'DEACTIVATED'
OVD = 'OVERDUE'

CARD_STATUSES = (
    (ACT, 'Active'),
    (DEACT, 'Deactivated'),
    (OVD, 'Overdue')
)


class Card(models.Model):
    series = models.PositiveSmallIntegerField('series', default=0)
    number = models.PositiveSmallIntegerField('number', default=0)
    release_date = models.DateTimeField('release at', auto_now_add=True)
    ending_date = models.DateTimeField('terminates at', auto_now_add=False)
    status = models.CharField('status', max_length=11,
                              choices=CARD_STATUSES,
                              default=DEACT
                              )
    
    def __str__(self) -> str:
        return f'{self.series}{self.number}'

class Payment(models.Model):
    card = models.ForeignKey(
        Card, on_delete=models.CASCADE,
        related_name='payments'
    )
    purchase_amount = models.DecimalField('purchase amout', max_digits=5, decimal_places=2)
    purchase_date = models.DateTimeField('purchase date', auto_now_add=True)
