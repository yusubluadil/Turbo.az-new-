from django.urls import path
from products import views

urlpatterns = [
  path('', views.index, name = "index"),
  path('upload/', views.image_upload_view, name = "img"),
  path('product/<int:pk>/', views.product_detail, name = "product_detail"),
  path('category-detail/<int:pk>/', views.category_detail, name = "category_detail"),
  path('product/search', views.search_product, name = "search_product"),
  path('select-product/<int:pk>', views.select_product, name = "select_product"),
  path('selected-product/', views.selected_product, name = "selected_product"),
]