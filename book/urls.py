from django.urls import path
from .views import *


urlpatterns = [
    path('', BookListView.as_view(), name='home'),
    path('generi/', GeneriListView.as_view(), name='generi'),
    path('autori/', AutoriListView.as_view(), name='autori'),
    path('azione/', AzioneListView.as_view(), name='azione'),
    path('giallo/', GialloListView.as_view(), name='giallo'),
    path('commedia/', CommediaListView.as_view(), name='commedia'),
    path('cucina/', CucinaListView.as_view(), name='cucina'),
    path('religioso/', ReligiosoListView.as_view(), name='religioso'),
    path('book_detail/<slug:slug>/', BookDetailView.as_view(), name='dettagli'),
    path('newbook/', BookCreateView.as_view(), name='newbook'),
    path('editbook/<int:pk>/', BookUpdateView.as_view(), name='editbook'),
    path('deletebook/<int:pk>/', BookDeleteView.as_view(), name='deletebook'),
]