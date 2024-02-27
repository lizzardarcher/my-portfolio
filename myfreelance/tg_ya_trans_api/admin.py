from django.contrib import admin
from tg_ya_trans_api.models import *


# Register your models here.
class IATA_ICAOAdmin(admin.ModelAdmin):
    list_display = ('country_code', 'region_name', 'iata', 'icao', 'airport')
    search_fields = ('country_code',)
    search_help_text = 'Код страны'


admin.site.register(IATA_ICAO, IATA_ICAOAdmin)
admin.site.register(TelegramScheduleUser)
admin.site.register(Airport)
admin.site.register(CitiesRU)
