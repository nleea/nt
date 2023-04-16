from django.urls import path,include,re_path
from .views.views import CreateTask,ViewTask,UpdateTask,DeleteTask

urlpatterns = [
    path("",ViewTask.as_view()),
    path("create/",CreateTask.as_view()),
    re_path(r"update/(?P<pk>[0-9]+)/$",UpdateTask.as_view()),
    re_path(r'^delete/(?P<pk>[0-9]+)/$',DeleteTask.as_view()),
    path("list/",include("apps.Task.api.views.listTaks.urls")),
    path("activity/",include("apps.Task.api.views.activity.urls"))
]
