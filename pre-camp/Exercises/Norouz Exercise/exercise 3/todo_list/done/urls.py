from django.urls import path

from .views import list_of_todo

urlpatterns = [
    path('todo-list/', list_of_todo),
]