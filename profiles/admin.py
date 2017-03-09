from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'birth_date', 'email', 'phone', 'status')
    prepopulated_fields = {"slug": ("full_name",)}
    readonly_fields = ('age_category',)
    search_fields = ('full_name',)
    date_hierarchy = 'birth_date'
    list_filter = ('status', 'sex', 'weight_category', 'age_category')
    list_per_page = 25
    fieldsets = [
        ("Основні дані", {'fields': ['full_name', 'image', 'bio', 'birth_date', 'status', 'weight_category']}),
        ("Контактна інформація", {'fields': ['city', 'email', 'phone']}),
        ("Додаткова інформація", {'fields': ['slug', 'sex', 'age_category']})
    ]
