from rest_framework import generics
from .models import UserInteraction
from .serializers import UserInteractionSerializer

class UserInteractionList(generics.ListCreateAPIView):
    queryset = UserInteraction.objects.all()
    serializer_class = UserInteractionSerializer

