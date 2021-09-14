from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

STATUS_CHOICES = (
    ('open', 'открытое'),
    ('closed', 'закрытое'),
    ('draft', 'черновик')
)

# Создать модель Product c полями: title, description, price и
# зарегистрировать его в админ панели. Создать записи в БД
# Создать вьюшки 3 способами (функцией, наследуясь от APIView и
# при помощи GenericView):


class Product(models.Model):
    title = models.CharField('title', max_length=150)
    description = models.TextField('Text')
    price = models.IntegerField('Price')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Product'

    def __str__(self):
        return self.title







