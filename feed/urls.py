from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^news/$', views.IndexView.as_view(), name='news_list'),
    url(r'^news/(?P<slug>[-\w]+)/$', views.NewDetailView.as_view(), name='new_detail'),
    url(r'^articles/$', views.ArticleListView.as_view(), name='articles_list'),
    url(r'^articles/(?P<slug>[-\w]+)/$', views.ArticleDetailView.as_view(), name='article_detail'),
]
