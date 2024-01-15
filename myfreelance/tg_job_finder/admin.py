from django.contrib import admin
from tg_job_finder.models import *
# Register your models here.
admin.site.register(TgChat)
admin.site.register(TgChannel)
admin.site.register(Settings)
admin.site.register(AllowedWord1Level)
admin.site.register(AllowedWord2Level)
admin.site.register(DisallowedWord)
admin.site.register(ExcludeWord)
