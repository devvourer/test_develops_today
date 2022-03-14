from django.db import models
from django.contrib.auth.models import User

from .querysets import ArticleQuerySet


class Article(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField(verbose_name="link to post")
    creation_date = models.DateTimeField(auto_now=True)
    amount_of_upvotes = models.PositiveSmallIntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = ArticleQuerySet.as_manager()

    def __str__(self):
        return f"{self.author} : {self.title}"


class Comment(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments"
    )
    content = models.CharField(max_length=500)
    creation_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.article} : {self.author_name} : {self.content}"
