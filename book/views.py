from django.shortcuts import render
from django.views.generic import ListView
from .models import Book, Autore

# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = 'home.html'

class AzioneListView(ListView):
    model = Book
    template_name = 'azione.html'
    def get_context_data(self, **kwargs):
            context= super().get_context_data(**kwargs)
            libri_Azione=Book.objects.filter(genere="Azione")
            context['libri_Azione']=libri_Azione
            return context

