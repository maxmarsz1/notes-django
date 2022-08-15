from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth.models import User

from notes.models import Note
from .serializers import NoteSerializer, UserSerializer


class ListCreateNotesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notes = Note.objects.filter(author=request.user)
        if notes.count():
            serialized = NoteSerializer(notes, many=True)
            return Response({"notes": serialized.data})
        else:
            return Response(status=status.HTTP_200_OK)

    def post(self, request):
        data = {
            "author": request.user.id,
            "body": request.data['body']
        }
        note = NoteSerializer(data=data)
        if note.is_valid():
            note.save()
            return Response(note.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UpdateDestroyNotesView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        try:
            note = Note.objects.get(id=pk)
            if request.user == note.author:
                note.body = request.data['body']
                note.save()
                serialized = NoteSerializer(note)
                return Response(serialized.data)
            return Response({'code': "You're not allowed here"}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            note = Note.objects.get(id=pk)
            if request.user == note.author:
                note.delete()
                return Response(status=status.HTTP_200_OK)
            return Response({'code': "You're not allowed here"}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)



class UserRegister(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        if User.objects.filter(username=request.data['username']).first(): return Response(status=status.HTTP_400_BAD_REQUEST, data={'Error': 'Username already taken'})
        if User.objects.filter(email=request.data['email']).first() is not None: return Response(status=status.HTTP_400_BAD_REQUEST, data={'Error': 'Email already taken'})
        if request.data['password'] != request.data['password1']: return Response(status=status.HTTP_400_BAD_REQUEST, data={'Error': 'Passwords mismatch'})
        user = User(username=request.data['username'], email=request.data['email'])
        user.set_password(request.data['password'])
        user.save()
        serialized = UserSerializer(user)

        return Response(serialized.data)


class BlacklistTokenView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'code': 'Success'})
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

