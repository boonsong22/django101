from django.urls import path
from products.views import ProductListView, ProductDetailView, CustomProductView
urlpatterns = [
    path("", ProductListView.as_view()),
    path("<int:pk>", ProductDetailView.as_view()),
    path('custom', CustomProductView.as_view())
]
