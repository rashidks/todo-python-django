from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    email=models.EmailField(unique=True)
class Task(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    description =models.TextField()