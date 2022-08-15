from rest_framework.serializers import ModelSerializer
from notes.models import Note
from django.contrib.auth.models import User


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'body']



class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']