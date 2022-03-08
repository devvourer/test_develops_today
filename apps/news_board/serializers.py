from rest_framework import serializers as srz

from .models import Article, Comment


class CommentSerializer(srz.ModelSerializer):
    author = srz.SlugRelatedField(
        slug_field="username", read_only=True
    )

    class Meta:
        model = Comment
        fields = ["content", "creation_date", "article", "author"]

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user

        return validated_data


class ArticleSerializer(srz.ModelSerializer):
    author = srz.SlugRelatedField(
        slug_field="username", read_only=True
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

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user

        return validated_data
