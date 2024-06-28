from django.db import models
from django.contrib.auth.models import User
from articles.models import Article

class Recommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    score = models.FloatField()

    


