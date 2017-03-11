from django.views.generic import TemplateView, ListView, DetailView
from .models import New, Article
from .mixins import FilterQuerysetMixin, UpdateObjectMixin
from profiles.models import Profile
from gallery.models import Photo, Video

class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'latest_news'
    queryset = New.published.all()[:3]

    def get_context_data(self):
        context = super().get_context_data()
        context['video'] = Video.objects.latest('created')
        context['photos'] = Photo.objects.random(5)
        return context

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
