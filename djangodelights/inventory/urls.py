from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('accounts/', include("django.contrib.auth.urls"), name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('ingredients/', views.IngredientView.as_view(), name='ingredients'),
    path('ingredients/new/', views.CreateIngredientView.as_view(), name='add_ingredient'),
    path('indredients/<pk>/update', views.UpdateIngredientView.as_view(), name='update_ingredient'),
    path('indredients/<pk>/delete', views.DeleteIngredientView.as_view(), name='delete_ingredient'),

    path('recipes/', views.RecipeView.as_view(), name='recipes'),
    path('recipes/new/', views.CreateRecipeView.as_view(), name='add_recipe'),
    path('recipes/<pk>/update', views.UpdateRecipeView.as_view(), name='update_recipe'),
    path('recipes/<pk>/delete', views.DeleteRecipeView.as_view(), name='delete_recipe'),

    path('menu/', views.MenuItemView.as_view(), name='menu'),
    path('menu/new/', views.CreateMenuItemView.as_view(), name='add_menu'),
    path('menu/<pk>/update', views.UpdateMenuItemView.as_view(), name='update_menu'),
    path('menu/<pk>/delete', views.DeleteMenuItemView.as_view(), name='delete_menu'),

    path('purchases/', views.PurchaseView.as_view(), name='purchases'),
    path('purchases/new/', views.CreatePurchaseView.as_view(), name='add_purchase'),

    path('reports/', views.ReportsView.as_view(), name='reports'),
]