from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):

    def __str__(self):
        return self.item_name

    user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_image = models.CharField(max_length=500,default="https://designshack.net/wp-content/uploads/placeholder-image-368x246.png")
    item_opening_hours = models.CharField(max_length = 10,default="07:00")
    item_shipping = models.BooleanField(default=False)
    item_shipping_available = models.BooleanField(default=False)
    item_sales = models.CharField(max_length=200,default="None")
    item_allowed_people = models.PositiveIntegerField(default=30)
    item_people_inside = models.PositiveIntegerField(default=1)