from rest_framework import serializers
from .models import Weight

class WeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weight
        fields = ('id', 'cargo_weight', 'takeoff_distance', 'takeoff_time', 'weight_to_lose')