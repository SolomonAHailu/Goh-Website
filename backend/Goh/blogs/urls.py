from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blogs.views import BlogViewSet

app_name = "blogs"
router = DefaultRouter()

router.register(r"", BlogViewSet)
urlpatterns = [
     path("", include(router.urls))
]
