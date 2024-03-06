from django.urls import path, include
from rest_framework.routers import DefaultRouter
from services.views import ServiceViewSet

app_name = "services"
router = DefaultRouter()

router.register(r"", ServiceViewSet)
urlpatterns = [
     path("", include(router.urls))
]
