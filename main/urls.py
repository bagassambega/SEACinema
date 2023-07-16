from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('movies', views.home, name='movies'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('account', views.account, name='account'),
]
