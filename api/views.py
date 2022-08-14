from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth.models import User

from notes.models import Note
from .serializers import NoteSerializer, UserSerializer


class ListNotes(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]


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

