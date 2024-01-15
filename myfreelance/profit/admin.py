from django.contrib import admin

from .models import *


admin.site.register(Project)
admin.site.register(AdditionalPayments)
admin.site.register(SupportPayments)
admin.site.register(Portfolio)

