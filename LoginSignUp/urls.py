from django.urls import path, include
from . import views
from book import urls as book_urls
urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.signup, name='signup'),
    path('accounts/login/', views.login, name='login'),
    path('accounts/', include("django.contrib.auth.urls")),
]