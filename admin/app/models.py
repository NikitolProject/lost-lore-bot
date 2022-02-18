from django.db import models


class BirthdaysEmployee(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200)
    birth_date = models.DateTimeField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class TemplatesForBirthday(models.Model):
    name = models.CharField(max_length=200)
    template = models.TextField()

    def __str__(self):
        return self.name


class AdsForEmployee(models.Model):
    TYPES_ADS = (
        (1, 'Объявление'),
        (2, 'Голосование')
    )

    name = models.CharField(max_length=200)
    type = models.IntegerField(choices=TYPES_ADS)
    description = models.TextField()
    date_of_publication = models.DateTimeField()

    def __str__(self):
        return self.name


class Channel(models.Model):
    TYPES_CHANNEL = (
        (1, 'Канал для публикации объявлений'),
        (2, 'FAQ канал (TODO)')
    )

    channel_id = models.CharField(max_length=200)
    type = models.IntegerField(choices=TYPES_CHANNEL)

    def __str__(self):
        return f'#{self.channel_id} - {self.type}'
