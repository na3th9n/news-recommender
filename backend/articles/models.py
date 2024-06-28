from django.db import models

# Create your models here.
class Article(models.Model):
    source = models.JSONField()
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=500)
    description = models.TextField()
    url = models.URLField()
    urlToImage = models.URLField(max_length=500)
    publishedAt = models.DateTimeField()
    content = models.TextField()

    def __str__(self):
        return self.title