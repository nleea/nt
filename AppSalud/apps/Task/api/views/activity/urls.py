from rest_framework.urls import path
from .views import ActivityView,ActivityTypeVIew,ActivityTypeCreate,CreateActivity

urlpatterns = [
    path("",ActivityView.as_view()),
    path("create/",CreateActivity.as_view()),
    path("type/",ActivityTypeVIew.as_view()),
    path("type/create/",ActivityTypeCreate.as_view())
]
