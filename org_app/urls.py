from rest_framework.routers import DefaultRouter
from .views import OrgViewSet

router = DefaultRouter()
router.register(r'orgs', OrgViewSet, basename='org')

urlpatterns = router.urls
