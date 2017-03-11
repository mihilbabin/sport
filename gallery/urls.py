from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.GalleryView.as_view(), name='gallery'),
    url(r'^videos/$', views.VideoListView.as_view(), name='videos_list'),
    url(r'^albums/$', views.AlbumListView.as_view(), name='albums_list'),
    url(r'^albums/(?P<slug>[\w-]+)', views.AlbumDetailView.as_view(), name='album_detail')
]
