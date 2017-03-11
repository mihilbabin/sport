from django.contrib import admin
from .models import Album, Photo, Video


class PhotosInline(admin.TabularInline):
    model = Photo
    extra = 5

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = [PhotosInline]
    list_display = ('__str__', 'count', 'status', 'created')
    list_filter = ('status',)
    search_fields = ('title',)
    date_hierarchy = 'created'
    list_per_page = 25
    prepopulated_fields = {'slug': ('title',)}



@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'status', 'created')
    search_fields = ('title',)
    date_hierarchy = 'created'
    list_filter = ('status',)
    list_per_page = 25
