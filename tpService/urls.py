"""tpService URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from rest_framework.schemas import get_schema_view

from tpApps.base import urls as base_url


schema_view = get_schema_view(
    title='性能长稳测平台',
    # renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer],
    permission_classes=()
)


urlpatterns = [
    path('admin/', admin.site.urls),

    # apps
    path('api/base/', include(base_url)),

    path(r'docs/', schema_view, name="docs"),
]
