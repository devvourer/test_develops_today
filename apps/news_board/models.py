from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    creation_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now_add=True)
    amount_of_upvotes = models.PositiveSmallIntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} : {self.title}"


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    creation_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.article} : {self.author_name} : {self.content}"
