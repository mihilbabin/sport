from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls import static
from django.conf import settings
from feed import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^gallery/', include('gallery.urls', namespace='gallery')),
    url(r'^feed/', include('feed.urls', namespace='feed')),
    url(r'^profiles/', include('profiles.urls', namespace='profiles')),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^contact/$', views.ContactView.as_view(), name='contact'),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
