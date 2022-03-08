from rest_framework import serializers as srz
from django.contrib.auth.models import User

from .models import Article, Comment


class CommentSerializer(srz.ModelSerializer):
    author = srz.SlugRelatedField(
        slug_field="username", queryset=User.objects.all(), read_only=False
    )

    class Meta:
        model = Comment
        fields = ["content", "creation_date", "article", "author"]


class ArticleSerializer(srz.ModelSerializer):
    author = srz.SlugRelatedField(
        slug_field="username", queryset=User.objects.all(), read_only=False
    )
    comments_count = srz.IntegerField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    amount_of_upvotes = srz.IntegerField(read_only=True)

    class Meta:
        model = Article
        fields = [
            "id",
            "title",
            "link",
            "author",
            "amount_of_upvotes",
            "creation_date",
            "comments_count",
            "comments",
        ]
