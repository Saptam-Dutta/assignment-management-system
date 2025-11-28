from rest_framework.routers import DefaultRouter
from .views import AssignmentTransactionViewSet

router = DefaultRouter()
router.register(r'transactions', AssignmentTransactionViewSet, basename='transactions')

urlpatterns = router.urls
