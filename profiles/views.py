from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from .models import Profile
from .forms import ProfileForm

class ProfileCreateView(SuccessMessageMixin, CreateView):
    model = Profile
    form_class = ProfileForm
    success_message = 'Ваша заявка на членство була успішно прийнята'

class ProfileDetailView(DetailView):
    model = Profile
