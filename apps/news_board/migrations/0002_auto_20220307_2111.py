# Generated by Django 3.2.12 on 2022-03-07 21:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("news_board", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="amount_of_upvotes",
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="article",
            name="link",
            field=models.URLField(verbose_name="link to post"),
        ),
        migrations.AlterField(
            model_name="comment",
            name="article",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="news_board.article",
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="author_name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
