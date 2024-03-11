from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Collection(models.Model):
    CHOICES = {
        'BD': 'bd',
        'FUNERAL': 'funeral',
        'WEDDING': 'wedding'
    }
    author = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=100)
    reason = models.CharField(max_length=10, choices=CHOICES)
    decsription = models.TextField(max_length=255)
    goal = models.BigIntegerField(null=True)
    collected = models.BigIntegerField()
    investors = models.IntegerField()
    image = models.ImageField()
    end_date = models.DateTimeField()
    # Список всех пожертвоваших думаю можно сделать используя инвесторов

    class Meta:
        verbose_name = "Сбор"
        verbose_name_plural = "Сборы"

    def __str__(self):
        return self.name


class Payment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # должна ли быть какая-то проверка, что человек не может внести больше всего сбора?
    # может ли он так сделать собственно?
    amount = models.BigIntegerField()

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        return f'Сумма платежа {self.amount}, плательщик {self.author}'
