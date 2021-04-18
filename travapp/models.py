from django.db import models


class Continent(models.Model):
    name = models.CharField('Название', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Континент'
        verbose_name_plural = 'Континенты'
        ordering = ['name']


class Country(models.Model):
    name = models.CharField('Название', max_length=50)
    continent = models.ForeignKey(
        Continent,
        null=True,
        on_delete=models.CASCADE,
    )
    SEA_CHOISES = (('Да', 'Да'), ('Нет', 'Нет'))
    sea = models.CharField('Наличие морских курортов', max_length=5, choices=SEA_CHOISES, null=True)
    MOUNTAIN_CHOISES = (('Да', 'Да'), ('Нет', 'Нет'))
    mountain = models.CharField('Наличие горнолыжных курортов', max_length=5, choices=MOUNTAIN_CHOISES, null=True)
    VISA_CHOISES = (('Да', 'Да'), ('Нет', 'Нет'))
    visa = models.CharField('Нужна ли виза беларусам', max_length=5, choices=VISA_CHOISES, null=True)
    description = models.TextField('Туристическое описание', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'
        ordering = ['name']


class Comment(models.Model):
    name = models.CharField('Короткий коммент', max_length=100)
    country = models.ForeignKey(
        Country,
        null=True,
        on_delete=models.CASCADE,
    )
    comment = models.TextField('Опишите ваш отдых', null=True)
    RATING_CHOISES = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'))
    rating = models.CharField('Оценка', max_length=5, choices=RATING_CHOISES, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['name']
