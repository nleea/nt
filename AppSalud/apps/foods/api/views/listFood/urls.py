from django.urls import path,re_path
from .views import CreateListFoods,DeleteListFoods,UpdateListFoods,ListFoodsView

urlpatterns = [
    path("",ListFoodsView.as_view()),
    path("create/",CreateListFoods.as_view()),
    re_path(r"update/(?P<pk>[0-9]+)/$",UpdateListFoods.as_view()),
    re_path(r'^delete/(?P<pk>[0-9]+)/$',DeleteListFoods.as_view())
]
