from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book, Autore
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


# Create your views here.
class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'home.html'

class GeneriListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'generi.html'
class AutoriListView(LoginRequiredMixin, ListView):
    model = Autore
    template_name = 'autori.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        autori = Autore.objects.all()
        context['autori'] = autori
        return context

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


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    template_name = 'newbook.html'
    fields = ['genere','title', 'author', 'year', 'pages', 'body', 'slug']


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    template_name = 'editbook.html'
    fields = ['genere','body']


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'deletebook.html'
    success_url = reverse_lazy("home")


class LibriperAutoriListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = "raccolta.html"
    def get_context_data(self, author_id=None, **kwargs):
        context = super().get_context_data(**kwargs)
        raccolta = Book.objects.filter(author_id=author_id)
        context['raccolta'] = raccolta
        return context


