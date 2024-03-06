from django.urls import path, include
from rest_framework.routers import DefaultRouter
from contact.views import ContactViewSet

app_name = "contact"
router = DefaultRouter()

router.register(r"", ContactViewSet)
urlpatterns = [
     path("", include(router.urls))
]
