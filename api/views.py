from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from notes.models import Note
from .serializers import NoteSerializer


class ListNotes(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer