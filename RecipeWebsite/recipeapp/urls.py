from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('registration/', views.registration, name='registration'),
    path('login/', auth_views.LoginView.as_view(next_page='/'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('show_five_recipe/', views.show_five_recipe, name='show_five_recipe'),
    path('show_full_recipe/<int:recipe_id>', views.show_full_recipe, name='show_full_recipe'),
]
