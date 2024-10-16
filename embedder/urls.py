from rest_framework.routers import DefaultRouter
from .views import EmbedViewSet, FaceCompareViewSet

router = DefaultRouter()
router.register(r"embeds", EmbedViewSet, basename="embed")
router.register(r"face-compare", FaceCompareViewSet, basename="face-compare")

urlpatterns = router.urls
