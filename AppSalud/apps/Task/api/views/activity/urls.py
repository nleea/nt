from django.urls import path,re_path
from .views import ActivityView,ActivityTypeVIew,ActivityTypeCreate,CreateActivity,DeleteActivity,DeleteTypeActivity,UpdateActivity,UpdateTypeActivity

urlpatterns = [
    path("",ActivityView.as_view()),
    path("create/",CreateActivity.as_view()),
    re_path(r"^update/(?P<pk>[0-9]+)/$",UpdateActivity.as_view()),
    re_path(r"^delete/(?P<pk>[0-9])/$",DeleteActivity.as_view()),
    path("type/",ActivityTypeVIew.as_view()),
    path("type/create/",ActivityTypeCreate.as_view()),
    re_path(r"^type/update/(?P<pk>[0-9]+)/$",UpdateTypeActivity.as_view()),
    re_path(r"^type/delete/(?P<pk>[0-9])/$",DeleteTypeActivity.as_view()),
]
