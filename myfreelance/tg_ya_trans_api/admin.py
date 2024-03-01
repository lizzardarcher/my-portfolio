from django.contrib import admin
from tg_ya_trans_api.models import *


# Register your models here.
class IATA_ICAOAdmin(admin.ModelAdmin):
    list_display = ('country_code', 'region_name', 'iata', 'icao', 'airport')
    search_fields = ('country_code',)
    search_help_text = 'Код страны'


class ConfigAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False


class TelegramScheduleUserAdmin(admin.ModelAdmin):
    list_display = ('date_joined', 'first_name', 'last_name', 'username')
    search_fields = ('first_name', 'last_name')
    search_help_text = 'Имя пользователя'
    ordering = ('date_joined',)


class LoggingTelegramUserAdmin(admin.ModelAdmin):
    list_display = ('date_created', 'tg_user', 'action')
    ordering = ('date_created',)


admin.site.register(IATA_ICAO, IATA_ICAOAdmin)
admin.site.register(TelegramScheduleUser, TelegramScheduleUserAdmin)
admin.site.register(Airport)
admin.site.register(CitiesRU)
admin.site.register(Config, ConfigAdmin)
admin.site.register(LoggingTelegramUser, LoggingTelegramUserAdmin)
