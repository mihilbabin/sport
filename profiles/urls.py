from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/$', views.ProfileCreateView.as_view(), name='profile_create'),
    url(r'^(?P<slug>[\w-]+)/$', views.ProfileDetailView.as_view(), name='profile_detail')
]
