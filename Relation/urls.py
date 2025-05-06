from rest_framework.routers import DefaultRouter
from .views import RelationViewSet
router = DefaultRouter()
router.register(r'relations', RelationViewSet)

urlpatterns = router.urls