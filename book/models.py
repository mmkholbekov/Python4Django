from django.db import models


class Book(models.Model):

    GENRE = (
        ('HORROR', 'HORROR'),
        ('FANTASY', 'FANTASY'),
        ('THRILLER', 'THRILLER'),
        ('BIOGRAPHY', 'BIOGRAPHY'),
        ('ADVENTURE', 'ADVENTURE')
    )

    title = models.CharField('Название книги', max_length=100)
    description = models.TextField('Описание книги')
    image = models.ImageField(upload_to='')
    quantity = models.PositiveIntegerField('Количество книг')
    genre = models.CharField(max_length=100, choices=GENRE)
    video = models.URLField()
    price = models.PositiveIntegerField('Цена билета', null=True)

    def __str__(self):
        return self.title
