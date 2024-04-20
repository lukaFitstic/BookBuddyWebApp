from django.urls import path
from .views import BookListView, AzioneListView, GeneriListView
urlpatterns = [
    path('', BookListView.as_view(), name='home'),
    path('generi/', GeneriListView.as_view(), name='generi'),
    path('azione/', AzioneListView.as_view(), name='azione'),
]