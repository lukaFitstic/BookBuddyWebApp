from django.urls import path
from .views import *
urlpatterns = [
    path('', BookListView.as_view(), name='home'),
    path('azione/', AzioneListView.as_view(), name='azione'),
    path('giallo/', GialloListView.as_view(), name='giallo')
]