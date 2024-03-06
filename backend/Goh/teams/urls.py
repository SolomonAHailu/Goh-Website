from django.urls import path, include
from rest_framework.routers import DefaultRouter
from teams.views import TeamViewSet

app_name = "Teams"
router = DefaultRouter()

router.register(r"", TeamViewSet)
urlpatterns = [
     path("", include(router.urls))
]
