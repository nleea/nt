from django.db import models
from .Base_model import BaseModel
from django.contrib.auth import get_user_model

User = get_user_model()

class Task(BaseModel):
    priority = models.CharField(max_length=256,choices=BaseModel.PRIORITY_CHOISES)
    status = models.BooleanField(default=True)
    task_user = models.ForeignKey(User,on_delete=models.CASCADE) 
    

class ListTask(BaseModel):
    task = models.ForeignKey(Task,on_delete=models.CASCADE,related_name="+")
    priority = models.CharField(max_length=256,choices=BaseModel.PRIORITY_CHOISES)

class ActivityType(BaseModel):
    name = models.CharField(max_length=50)

class Activity(BaseModel):
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    hours = models.CharField(max_length=10)
    listTask = models.ForeignKey(ListTask,on_delete=models.CASCADE)
    typeActivity = models.ForeignKey(ActivityType,on_delete=models.CASCADE)
    repeat = models.BooleanField()

class Exercises(BaseModel):
    duration = models.IntegerField()
    sets = models.IntegerField()
    intensity = models.CharField(max_length=20,choices=BaseModel.PRIORITY_CHOISES)
    activity = models.ForeignKey(Activity,on_delete=models.CASCADE)


class Hikes(BaseModel):
    pasos = models.IntegerField()
    exercise = models.ForeignKey(Exercises,on_delete=models.CASCADE)

class Meditation(BaseModel):
    duration= models.CharField(max_length=20)
    activity = models.ForeignKey(Activity,on_delete=models.CASCADE)