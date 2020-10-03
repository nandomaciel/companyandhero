from django.urls import path, include
from .views import FuncionariosViewSets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("funcionario", FuncionariosViewSets, basename="funcionario")

urlpatterns = [
    path('', include(router.urls)),
]