from django.db import models

plane_weight = 35000


# Create your models here.
class Weight(models.Model):
    cargo_weight = models.IntegerField(default=0)
    value = getattr(cargo_weight, 'name')
    print(value)
    takeoff_distance = (0.098 * (value +  plane_weight))
    takeoff_time = (0.0014 * (cargo_weight + plane_weight))
    weight_to_lose = (cargo_weight - ((60 / 0.0014) - plane_weight)) if takeoff_time > 60 else 0
