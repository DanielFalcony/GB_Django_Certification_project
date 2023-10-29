from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('registration/', views.registration, name='registration'),
    path('login/', auth_views.LoginView.as_view(next_page='/'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
