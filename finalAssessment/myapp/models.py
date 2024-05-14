# finalAssessment>myapp>models.py
from django.db import models
from django.contrib.auth.models import User

class TravelPlan(models.Model):
    destination = models.CharField(max_length=100)
    description = models.TextField()
    travel_date_from = models.DateField()
    travel_date_to = models.DateField()

class TripSchedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    travel_plan = models.ForeignKey(TravelPlan, on_delete=models.CASCADE)


