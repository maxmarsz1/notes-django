from django.urls import path
from .views import ListNotes

urlpatterns = [
    path('notes/', ListNotes.as_view({'get': 'list', 'post': 'create'}), name='notes-list'),
    path('notes/<int:pk>/', ListNotes.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'}), name='note'),
]
