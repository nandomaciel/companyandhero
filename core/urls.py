"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

API_TITLE = "API Company and Hero "
API_DESCRIPTION = "Empresas e Funcionarios"

admin.AdminSite.site_header = "Company and Hero"
admin.AdminSite.site_title = "Company"
admin.AdminSite.index_title = "Company and Hero"

# schema_view = get_schema_view(
#     openapi.Info(
#         title="Company and Hero",
#         default_version='v1',
#         description="Teste",
#         terms_of_service="https://companyandhero.heroku.com",
#         contact=openapi.Contact(email="nandormaciel@gmail.com"),
#         license=openapi.License(name="BSD License"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('empresa.urls')),
    path('api/v1/', include('funcionario.urls')),
    # path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
