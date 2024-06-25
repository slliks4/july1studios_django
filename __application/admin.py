from django.contrib import admin
from .models import Vacancy,Application,Jobs_available

admin.site.register(Vacancy)
admin.site.register(Application)
admin.site.register(Jobs_available)