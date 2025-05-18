from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReparacionViewSet

router = DefaultRouter()
router.register(r'reparaciones', ReparacionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
