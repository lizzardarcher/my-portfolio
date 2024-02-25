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
