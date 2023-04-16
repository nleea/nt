from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class BaseModel(models.Model):
    PRIORITY_CHOISES = (("L","LOW"),("M","MEDIUN"),("H","HIGHT"))
    name = models.CharField(max_length=256,null=True,blank=True)
    createBy = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="+", blank=True, null=True
    )
    updateBy = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="+", blank=True, null=True
    )
    createAt = models.DateTimeField(auto_created=True, blank=True, null=True)
    updateAt = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        abstract = True