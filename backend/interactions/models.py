from django.db import models
from django.contrib.auth.models import User
from articles.models import Article

class UserInteraction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    interaction_type = models.CharField(max_length=10)  # e.g., 'like', 'dislike', 'save'
    timestamp = models.DateTimeField(auto_now_add=True)



