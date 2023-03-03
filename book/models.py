from django.db import models


class Book(models.Model):

    GENRE = (
        ('HORROR', 'HORROR'),
        ('COMEDY', 'COMEDY'),
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


class RatingBook(models.Model):
    RATING = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    choise_book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comment_object')
    rate = models.IntegerField('Оценка: ', choices=RATING)
    comment = models.TextField('Комментарий: ')
    created_date = models.DateTimeField(auto_now_add=True)
