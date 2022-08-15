from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import UserRegister, BlacklistTokenView, ListCreateNotesView, UpdateDestroyNotesView

urlpatterns = [
    # path('notes/', ListNotes.as_view({'get': 'list', 'post': 'create'}), name='notes-list'),
    # path('notes/<int:pk>/', ListNotes.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'}), name='note'),
    path('notes/', ListCreateNotesView.as_view()),
    path('notes/<int:pk>/', UpdateDestroyNotesView.as_view()),
    path('register/', UserRegister.as_view(), name='user_registrations'),
    path('logout/', BlacklistTokenView.as_view(), name='token_blacklist'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
