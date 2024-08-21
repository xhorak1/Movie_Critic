from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import custom_logout


urlpatterns = [
    path('', views.index, name='index'),
    path('movies/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='reviews/login.html'), name='login'),
    path('logout/', custom_logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('', views.index, name='index'),
    path('movie-database/', views.movie_database, name='movie_database'),
    path('about/', views.about_movie_critic, name='about_movie_critic'),
    path('privacy/', views.privacy_policy, name='privacy_policy'),
    path('movie/<int:movie_id>/review/', views.submit_review, name='submit_review'),

]