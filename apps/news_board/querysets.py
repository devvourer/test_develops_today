from django.db import models


class ArticleQuerySet(models.QuerySet):
    def with_comments_count(self):
        return self.annotate(comments_count=models.Count("comments"))
