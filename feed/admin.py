from django.contrib import admin
from .models import New


@admin.register(New)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
