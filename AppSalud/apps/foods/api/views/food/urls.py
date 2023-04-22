from django.urls import path,include,re_path
from .views import CreateFood,DeleteFood,FoodView,UpdateFood

urlpatterns = [
    path("",FoodView.as_view()),
    path("create/",CreateFood.as_view()),
    re_path(r"update/(?P<pk>[0-9]+)/$",UpdateFood.as_view()),
    re_path(r'^delete/(?P<pk>[0-9]+)/$',DeleteFood.as_view())
]
