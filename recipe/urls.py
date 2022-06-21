from django.urls import path

from recipe import views


app_name='recipe'
urlpatterns = [
    path('recipes', views.RecipeListView.as_view(), name='recipe-list'),
    path('recipe/add/', views.RecipeCreateView.as_view(), name='recipe-add'),
    path('recipe/<int:pk>/detail', views.RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipe/<int:pk>/update', views.RecipeUpdateView.as_view(), name='recipe-update'),
    path('recipe/<int:pk>/delete', views.RecipeDeleteView.as_view(), name='recipe-delete'),
]