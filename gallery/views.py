from django.views.generic import TemplateView, ListView, DetailView
from .models import Album, Video
from feed.mixins import FilterQuerysetMixin

class GalleryView(TemplateView):
    template_name = 'gallery/gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['videos'] = Video.published.all()[:3]
        context['albums'] = Album.published.all()[:3]
        return context


class VideoListView(FilterQuerysetMixin, ListView):
    model = Video
    context_object_name = 'videos_list'

class AlbumListView(FilterQuerysetMixin, ListView):
    model = Album
    context_object_name = 'albums_list'


class AlbumDetailView(FilterQuerysetMixin, DetailView):
    context_object_name = 'album'
    model = Album
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.select_related()
