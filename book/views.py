from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book, Autore
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'home.html'

class GeneriListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'generi.html'


class AzioneListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'azione.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        libri_Azione = Book.objects.filter(genere="Azione")
        context['libri_Azione'] = libri_Azione
        return context


class GialloListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'giallo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        libri_Giallo = Book.objects.filter(genere="Giallo")
        context['libri_Giallo'] = libri_Giallo
        return context


class CommediaListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'commedia.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        libri_Commedia = Book.objects.filter(genere="Commedia")
        context['libri_Commedia'] = libri_Commedia
        return context


class CucinaListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'cucina.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        libri_Cucina = Book.objects.filter(genere="Cucina")
        context['libri_Cucina'] = libri_Cucina
        return context


class ReligiosoListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'religioso.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        libri_Religioso = Book.objects.filter(genere="Religioso")
        context['libri_Religioso'] = libri_Religioso
        return context


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'dettagli.html'
