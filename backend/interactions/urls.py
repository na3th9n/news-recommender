from django.urls import path
from .views import UserInteractionList

urlpatterns = [
    path('interactions/', UserInteractionList.as_view(), name='user-interaction-list'),
]
