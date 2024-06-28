from rest_framework import generics
from .models import Recommendation
from .serializer import RecommendationSerializer

class RecommendationList(generics.ListCreateAPIView):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer
