from rest_framework.urls import path
from .listTask import CreateListTask,ListTaskView

urlpatterns = [
    path("",ListTaskView.as_view()),
    path("create/",CreateListTask.as_view())
]
