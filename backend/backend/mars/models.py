from django.db import models

# Create your models here.
class Mars(models.Model) : 
    superficy = models.CharField(max_length=50)
    gravity  = models.CharField(max_length=50)
    distance_from_sun = models.CharField(max_length=50)
    duration_of_day = models.CharField(max_length=50)
    mass = models.CharField(max_length=50)
    age  = models.CharField(max_length=50)
class Moon(models.Model) : 
    name = models.CharField(max_length=50)
    planet = models.ForeignKey(Mars , on_delete=models.CASCADE , related_name='moons')