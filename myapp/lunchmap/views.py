from django.views import  generic
from .models import Category, Shop
from django.urls import reverse_lazy


class IndexView(generic.ListView):
    model = Shop


class DetailView(generic.DetailView):
    model = Shop


class CreateView(generic.CreateView):
    model = Shop
    fields = "__all__"


class UpdateView(generic.UpdateView):
    model = Shop
    fields = "__all__"


class DeleteView(generic.edit.DeleteView):
    model = Shop
    success_url = reverse_lazy('lunchmap:index')