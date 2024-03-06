from django.urls import path, include
from rest_framework.routers import DefaultRouter
from projects.views import ProjectViewSet

app_name = "projects"
router = DefaultRouter()

router.register(r"", ProjectViewSet)
urlpatterns = [
     path("", include(router.urls))
]
