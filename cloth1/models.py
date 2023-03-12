from telnetlib import STATUS
from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('На обработке', 'На обработке'),
        ('Выехал', 'Выехал'),
        ('Доставлен', 'Доставлен')
    )


customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
product = models.ForeignKey(Product, on_delete=models.CASCADE)
date_created = models.CharField(max_length=100, choices=STATUS)
status = models.CharField(max_length=100, choices=STATUS)


def __str__(self):
    return self.product.name
