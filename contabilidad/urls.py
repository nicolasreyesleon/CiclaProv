from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovimientoContableViewSet, resumen_contable

router = DefaultRouter()
router.register(r'contabilidad', MovimientoContableViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('resumen/', resumen_contable),
]
