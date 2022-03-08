from test_develops_today.celery import app

from .models import Article


@app.task()
def upvote_article(article_id: int) -> None:
    try:
        article = Article.objects.get(id=article_id)
        article.amount_of_upvotes += 1
        article.save()
    except Article.DoesNotExist as e:
        raise e
