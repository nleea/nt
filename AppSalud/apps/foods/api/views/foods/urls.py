from django.urls import path,re_path
from .views import CreateFoods,DeleteFoods,FoodsView,UpdateFoods

urlpatterns = [
    path("",FoodsView.as_view()),
    path("create/",CreateFoods.as_view()),
    re_path(r"update/(?P<pk>[0-9]+)/$",UpdateFoods.as_view()),
    re_path(r'^delete/(?P<pk>[0-9]+)/$',DeleteFoods.as_view())
]
