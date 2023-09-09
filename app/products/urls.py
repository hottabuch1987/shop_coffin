from django.urls import path, include
from products import views




urlpatterns = [
    path('latest-products/', views.LatestProductsList.as_view()),
    path('search/', views.search),
    path('<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    path('<slug:category_slug>/', views.CategoryDetail.as_view()),
]