"""
URL configuration for kami project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view


from api import viewsets


router = DefaultRouter()
router.register(r'planes', viewsets.PlaneViewset, basename='planes')


urlpatterns = router.urls
urlpatterns.append(
    path(
        'openapi/',
        get_schema_view(
            title="KAMI Airlines",
            description="API for KAMI Airlines REST API.",
            version="1.0.0",
        ),
        name='openapi-schema'
    )
)
urlpatterns.append(
    path(
        "docs/",
        TemplateView.as_view(
            template_name="swagger-ui.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="swagger-ui",
    ),
)