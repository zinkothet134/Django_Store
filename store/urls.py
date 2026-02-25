from django.urls import path
from . import views

urlpatterns = [
    # Home can show store page (or a separate homepage later)
    # path('', views.store, name='home'),

    # Store: all products
    path('', views.store, name='store'),

    # Store: filter by category
    path('category/<slug:category_slug>/', views.store, name='products_by_category'),

    # Product detail
    path('store/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),

    # Search
    path('store/search/', views.search, name='search'),
    
] 