from django.urls import path,re_path
from .listTask import CreateListTask,ListTaskView,DeleteListTask,UpdateListTaks

urlpatterns = [
    path("",ListTaskView.as_view()),
    path("create/",CreateListTask.as_view()),
    re_path(r"^update/(?P<pk>[0-9]+)/$",UpdateListTaks.as_view()),
    re_path(r"^delete/(?P<pk>[0-9])/$",DeleteListTask.as_view()),
]
