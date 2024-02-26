from django.db import models


# Create your models here.
class IATA_ICAO(models.Model):
    country_code = models.CharField(max_length=2, verbose_name="Код страны")
    region_name = models.CharField(max_length=1000, verbose_name="Регион")
    iata = models.CharField(max_length=3, verbose_name="IATA")
    icao = models.CharField(max_length=4, verbose_name="ICAO")
    airport = models.CharField(max_length=1000, verbose_name="Аэропорт ")

    def __str__(self):
        return self.country_code + ' ' + self.region_name + ' ' + self.iata + ' ' + self.icao + ' ' + self.airport

    class Meta:
        verbose_name = 'IATA ICAO'
        verbose_name_plural = 'IATA ICAO'


class TelegramScheduleUser(models.Model):
    date_joined = models.DateTimeField(auto_now_add=True)
    telegram_id = models.BigIntegerField(verbose_name="Telegram ID", primary_key=True)
    first_name = models.CharField(max_length=100, null=True, blank=True, default='', verbose_name="First Name")
    last_name = models.CharField(max_length=100, null=True, blank=True, default='', verbose_name="Last Name")
    username = models.CharField(max_length=100, null=True, blank=True, default='', verbose_name="username")

    selected_station    = models.CharField(max_length=100, null=True, blank=True, default='', verbose_name="")
    selected_date       = models.CharField(max_length=100, null=True, blank=True, default='', verbose_name="")
    selected_shift_type = models.CharField(max_length=100, null=True, blank=True, default='', verbose_name="")
    selected_direction  = models.CharField(max_length=100, null=True, blank=True, default='', verbose_name="")

    def __str__(self):
        if self.first_name:
            fn = self.first_name
        else:
            fn = ''
        if self.last_name:
            ln = self.last_name
        else:
            ln = ''
        return fn + ' ' + ln

    class Meta:
        verbose_name = 'Пользователь телеграм'
        verbose_name_plural = 'Пользователи телеграм'