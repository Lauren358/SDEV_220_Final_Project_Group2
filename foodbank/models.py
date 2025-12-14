from django.db import models
from django.conf import settings
from django.utils import timezone



class Inventory(models.Model):
    food_name = models.CharField(max_length=30)
    food_total = models.IntegerField()

    def __str__(self):
        return self.food_name

#class Donation(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL)
    #food_name = models.CharField(max_length=30)
    #food_total = models.IntegerField()
    #donation_date = models.DateTimeField(default=timezone.now)