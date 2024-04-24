from django.db import models
from django.db.models import UniqueConstraint


class Place(models.Model):
    place_id = models.CharField(max_length=100, unique=True, verbose_name='Идентификатор')
    place_name = models.CharField(max_length=35, verbose_name='Название')
    total_purchases = models.PositiveIntegerField(verbose_name='Количество покупок', default=0)
    average_receipt = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Средний чек',
                                          default=0.00)
    total_nds = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Сумма НДС',
                                    default=0.00)
    total_tips = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Сумма чаевых',
                                     default=0.00)

    def __str__(self):
        return self.place_name

    class Meta:
        verbose_name = "Аналитика по месту покупки"
        verbose_name_plural = "Аналитика по местам покупок"


class Category(models.Model):
    name = models.CharField(max_length=35, verbose_name='Название')
    total_spent = models.DecimalField(max_digits=15, decimal_places=2,
                                      verbose_name='Сумма потраченная на категорию за промежуток времени',
                                      default=0.00)
    average_receipt = models.DecimalField(max_digits=15, decimal_places=2,
                                          verbose_name='Средний чек по категории', default=0.00)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name="Место покупки",
                              related_name='categories')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Аналитика по категории"
        verbose_name_plural = "Аналитика по категориям"
        constraints = [
            UniqueConstraint(
                fields=('name', 'place',),
                name='Unique name and place', ),
        ]


class Check(models.Model):
    check_json = models.JSONField(verbose_name="Чек")
    is_calculated = models.BooleanField(default=False, verbose_name="Посчитан")

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = "Чек для аналитики"
        verbose_name_plural = "Чеки для аналитики"
