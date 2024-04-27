from urllib import request

from django.http import JsonResponse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book, Autore, ToRead
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect


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


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    template_name = 'newbook.html'
    fields = ['genere', 'title', 'author', 'year', 'pages', 'body', 'slug']


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    template_name = 'editbook.html'
    fields = ['genere', 'body']


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'deletebook.html'
    success_url = reverse_lazy("home")


class AddBookView(LoginRequiredMixin, View):
    def post(self, request, book_id):
        user = request.user
        book = get_object_or_404(Book, pk=book_id)
        ToRead.objects.create(user=user, book=book)

        return redirect(book.get_absolute_url())


class ListListView(LoginRequiredMixin, ListView):
    model = ToRead
    template_name = 'toreadlist.html'
    context_object_name = 'user'

    def get_queryset(self):
        user = self.request.user
        user__id = user.id
        return ToRead.objects.filter(user__id=user__id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        user__id = user.id
        book_list = ToRead.objects.filter(user__id=user__id)
        context['list'] = book_list
        return context