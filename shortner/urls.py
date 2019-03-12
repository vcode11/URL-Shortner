from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'shortner'

urlpatterns = [
    path('login/', views.userlogin, name="login"),
    path('', views.index, name="index"),
    path('log_out/', views.userlogout, name="userlogout"),
    path('sign_up/', views.usersignup, name="signup"),
    path('<short_url>/', views.redirect, name="redirect"),

]
