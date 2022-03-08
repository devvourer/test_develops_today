from rest_framework.routers import SimpleRouter
from .views import ArticleViewSet, CommentViewSet

router = SimpleRouter()
router.register("article", ArticleViewSet)
router.register("comment", CommentViewSet)

urlpatterns = router.urls
