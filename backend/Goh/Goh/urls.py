
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/blogs/", include("blogs.urls", namespace="blogs")),
    # path("api/products/", include("products.urls", namespace="products")),
    # path("api/user/orders/", include("orders.urls", namespace="orders")),
    # path("api/user/payments/", include("payment.urls", namespace="payment")),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
  
]

# Media Assets
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Schema URLs
urlpatterns += [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]