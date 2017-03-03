from django.views.generic import TemplateView, ListView, DetailView
from .models import New, Article
from .mixins import FilterQuerysetMixin, UpdateObjectMixin


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'latest_news'
    queryset = New.published.all()[:3]

class NewListView(FilterQuerysetMixin, ListView):
    context_object_name = 'news_list'
    model = New

class ArticleListView(FilterQuerysetMixin, ListView):
    context_object_name = 'articles_list'
    model = Article

class NewDetailView(FilterQuerysetMixin, UpdateObjectMixin, DetailView):
    context_object_name = 'new'
    model = New

class ArticleDetailView(FilterQuerysetMixin, UpdateObjectMixin, DetailView):
    context_object_name = 'article'
    model = Article

class AboutView(TemplateView):
    template_name = 'about.html'

class ContactView(TemplateView):
    template_name = 'contact.html'
