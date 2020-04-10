from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django_countries import countries
from . import models, forms


class HomeView(ListView):
    """ HomeView Definition """

    model = models.Room
    page_kwarg = "page"
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


class RoomDetail(DetailView):
    model = models.Room


def search(request):

    form = forms.SearchForm()
    return render(request, "rooms/search.html", {"form": form,})
