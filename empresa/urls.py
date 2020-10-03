from django.urls import path, include
from .views import EmpresasViewSets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("empresa", EmpresasViewSets, basename="empresa")


urlpatterns = [
    path('', include(router.urls)),
]