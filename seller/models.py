from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# 실제로 할 때는 구조화 시켜서 모델을 만들어야함
# class Category(models.Model):
#     name=models.CharField(max_length=200)

class Food(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    price = models.IntegerField()
    description = models.TextField()
    image_url=models.URLField()