from django.urls import path,re_path
from .views import Login,Register,Update

urlpatterns = [
    path("login/",Login.as_view()),
    path("register/",Register.as_view()),
    path('update/<int:pk>/',Update.as_view()),
    path('update/password/<int:pk>/',Update.as_view()),
]
