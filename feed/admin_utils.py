from django.contrib import admin
from django.utils import timezone
from django.db.models import Q

class PublishedListFilter(admin.SimpleListFilter):
    title = "Опубліковано на сайті"
    parameter_name = "published"

    def lookups(self, request, modeladmin):
        return (
            ('published', 'Так'),
            ('draft', 'Ні')
        )

    def queryset(self, request, queryset):
        if self.value() == 'published':
            return queryset.filter(status='published').filter(publish_date__lte=timezone.now())
        if self.value() == 'draft':
            return queryset.filter(Q(status='draft')|Q(publish_date__gt=timezone.now()))
        return queryset

def make_published(modeladmin, request, queryset):
    queryset.update(status='published')
make_published.short_description = "Позначити, як опубліковані"

def make_drafted(modeladmin, request, queryset):
    queryset.update(status='draft')
make_drafted.short_description = "Позначити, як редаговані"
