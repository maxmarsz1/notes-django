from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from django.contrib.auth.models import User

from notes.models import Note
from .serializers import NoteSerializer, UserSerializer


class ListNotes(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class UserRegister(APIView):
    def post(self, request):
        user = User(username=request.data['username'], email=request.data['email'])
        if request.data['password1'] != request.data['password2']: return Response(status=status.HTTP_400_BAD_REQUEST, data={'Error': 'Passwords mismatch'})
        user.set_password(request.data['password1'])
        user.save()
        serialized = UserSerializer(user)

        return Response(serialized.data)
