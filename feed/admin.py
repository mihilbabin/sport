from django.contrib import admin
from django.utils import timezone
from .models import New, Article, Tag
from .admin_utils import make_published, make_drafted, PublishedListFilter


class CommonAdminMixin:
    list_display = ('__str__', 'publish_date', 'created', 'status', 'is_published')
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ('created', 'updated')
    search_fields = ('title',)
    date_hierarchy = 'publish_date'
    list_filter = ('status', 'publish_date', PublishedListFilter)
    actions = [make_published, make_drafted]
    list_per_page = 25
    fieldsets = [
        ("Основні дані", {'fields': ['title', 'content', 'image', 'views', 'status']}),
        ("Іформація про дату", {'fields': ['publish_date', 'created', 'updated']}),
        ("Додаткова інформація", {'fields': ['user', 'slug'], 'classes': ['collapse']})
    ]


@admin.register(New)
class NewAdmin(CommonAdminMixin, admin.ModelAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(CommonAdminMixin, admin.ModelAdmin):
    fieldsets = [
        ("Основні дані", {'fields': ['title', 'content', 'image', 'status', 'tags', 'views', ]}),
        ("Іформація про дату", {'fields': ['publish_date', 'created', 'updated']}),
        ("Додаткова інформація", {'fields': ['user', 'slug'], 'classes': ['collapse']})
    ]
    list_filter = (PublishedListFilter, 'tags', 'publish_date')
    filter_horizontal = ('tags',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created')
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ('created', 'updated')
    search_fields = ('name',)
    fieldsets = [
        ("Основні дані", {'fields': ['name']}),
        ("Іформація про дату", {'fields': ['created', 'updated']}),
        ("Додаткова інформація", {'fields': ['slug'], 'classes': ['collapse']})
    ]
