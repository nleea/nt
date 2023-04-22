from django.urls import path,include

urlpatterns = [
    path("",include("apps.foods.api.views.foods.urls")),
    path("list/",include("apps.foods.api.views.listFood.urls")),
    path("ingredients/",include("apps.foods.api.views.food.urls"))
]
