from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BicicletaViewSet

router = DefaultRouter()
router.register(r'bicicletas', BicicletaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
