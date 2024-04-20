from django.shortcuts import render
from django.views.generic import ListView
from .models import Book, Autore


# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = 'home.html'

class GeneriListView(ListView):
    model = Book
    template_name = 'generi.html'


class AzioneListView(ListView):
    model = Book
    template_name = 'azione.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        libri_Azione = Book.objects.filter(genere="Azione")
        context['libri_Azione'] = libri_Azione
        return context


class GialloListView(ListView):
    model = Book
    template_name = 'giallo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        libri_Giallo = Book.objects.filter(genere="Giallo")
        context['libri_Giallo'] = libri_Giallo
        return context


class CommediaListView(ListView):
    model = Book
    template_name = 'commedia.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        libri_Commedia = Book.objects.filter(genere="Commedia")
        context['libri_Commedia'] = libri_Commedia
        return context


class CucinaListView(ListView):
    model = Book
    template_name = 'cucina.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        libri_Cucina = Book.objects.filter(genere="Cucina")
        context['libri_Cucina'] = libri_Cucina
        return context


class ReligiosoListView(ListView):
    model = Book
    template_name = 'religioso.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        libri_Religioso = Book.objects.filter(genere="Religioso")
        context['libri_Religioso'] = libri_Religioso
        return context


