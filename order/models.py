from django.db import models
from seller.models import Food
from django.contrib.auth.models import User
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    # 수량
    amount = models.IntegerField(default=0)
    # 금액    
    total_price = models.IntegerField(default=0)


class Order(models.Model):
    pass