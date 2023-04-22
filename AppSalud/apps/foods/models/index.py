from django.db import models
from django.contrib.auth import get_user_model
from .Base_model import BaseModel
User = get_user_model()

class Foods(BaseModel):
    user_foods = models.ForeignKey(User,on_delete=models.CASCADE)
    

class ListFoods(BaseModel):
    foods_list = models.ForeignKey(Foods,on_delete=models.CASCADE)


class Food(BaseModel):
    nutrients = models.CharField(max_length=256)
    carbohydrate = models.CharField(max_length=256)
    amount = models.IntegerField()
    list_food = models.ForeignKey(ListFoods,on_delete=models.CASCADE)