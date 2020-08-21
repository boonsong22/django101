from django.contrib import admin
from django.urls import path, include

from products.views import ProductListView, ProductDetailView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("products/", include('products.urls')),
]
