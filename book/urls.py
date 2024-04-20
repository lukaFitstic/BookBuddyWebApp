from django.urls import path
from .views import BookListView, AzioneListView
urlpatterns = [
    path('', BookListView.as_view(), name='home'),
    path('azione/', AzioneListView.as_view(), name='azione'),
]