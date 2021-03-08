from rest_framework import routers
from .views import FileViewSet


router = routers.DefaultRouter()
router.register(r'file', FileViewSet)