from django.db import models
from django.contrib.auth.models import User
ADMIN = 1
VIP = 2
CLIENT = 3

USER_TYPE = (
    (ADMIN, "ADMIN"),
    (VIP, "VIP"),
    (CLIENT, "CLIENT")
)

MALE = 1
FEMALE = 2

GENDER_TYPE = (
    (MALE, "MALE"),
    (FEMALE, "FEMALE"),
)

ASIA = 1
EUROPE = 2
AMERICA = 3
AFRICA = 4


REGION_TYPE = (
    (ASIA, "ASIA"),
    (EUROPE, "EUROPE"),
    (AMERICA, "AMERICA"),
    (AFRICA, "AFRICA"),

)


class CustomUser(User):
    class Meta:
        verbose_name = 'Ползователь'
        verbose_name_plural = 'Ползователи'

    user_type = models.IntegerField(choices=USER_TYPE, verbose_name='Тип пользователья')
    phone_number = models.CharField('Номер телефона', max_length=16)
    gender = models.IntegerField(choices=GENDER_TYPE, verbose_name='Пол')
    age = models.PositiveIntegerField()
    region = models.IntegerField(choices=REGION_TYPE, verbose_name='Ваш регион')
    country = models.CharField('Страна', max_length=15)
    city = models.CharField('Город проживания', max_length=20)
    address = models.CharField('Адрес', max_length=30)
