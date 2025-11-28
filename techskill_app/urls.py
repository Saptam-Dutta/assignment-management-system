from rest_framework.routers import DefaultRouter
from .views import TechSkillViewSet

router = DefaultRouter()
router.register(r'techskills', TechSkillViewSet, basename='techskills')

urlpatterns = router.urls
