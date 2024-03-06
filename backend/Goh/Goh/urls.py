from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/blogs/", include("blogs.urls", namespace="blogs")),
    path("api/contact/", include("contact.urls", namespace = "contact")),
    path("api/projects/", include("projects.urls", namespace = "projects")),
    path("api/services/", include("services.urls", namespace = "services")),
    path("api/teams/", include("teams.urls", namespace = "teams")),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]

# Spectacular API and Swagger UI
urlpatterns += [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("", SpectacularSwaggerView.as_view(url_name="schema")),
]


# Media Assets
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns = [
#     ...
#     path('api-auth/', include('rest_framework.urls')),  # For login/logout
#     path('swagger-docs/', include('rest_framework_swagger.urls')),  # Swagger documentation
# ]
