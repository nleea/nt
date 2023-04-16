from django.urls import path,include
from .views.views import CreateTask,ViewTask

urlpatterns = [
    path("",ViewTask.as_view()),
    path("create/",CreateTask.as_view()),
    path("list/",include("apps.Task.api.views.listTaks.urls")),
    path("activity/",include("apps.Task.api.views.activity.urls"))
]
