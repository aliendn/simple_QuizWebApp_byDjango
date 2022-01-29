from django.urls import path
from .views import quiz

urlpatterns = [
    path('<str:username>/', quiz)
]
