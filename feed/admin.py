from django.contrib import admin
from django.utils import timezone
from .models import New
from .admin_utils import make_published, PublishedListFilter


@admin.register(New)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'publish_date', 'created', 'status', 'is_published')
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ('created', 'updated')
    search_fields = ('title',)
    date_hierarchy = 'publish_date'
    list_filter = ('status', 'publish_date', PublishedListFilter)
    actions = [make_published]
    fieldsets = [
        ("Основні дані", {'fields': ['title', 'content', 'image', 'views', 'status']}),
        ("Іформація про дату", {'fields': ['publish_date', 'created', 'updated']}),
        ("Додаткова інформація", {'fields': ['user', 'slug'], 'classes': ['collapse']})
    ]
