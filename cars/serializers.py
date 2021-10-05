from rest_framework import serializers
from .models import Car
from django.contrib.auth import get_user_model
User = get_user_model()

class CarSerializer(serializers.ModelSerializer):

    # price = serializers.DecimalField()
    # name = serializers.CharField()
    # color = serializers.CharField()
    # motor = serializers.CharField()
    # drive_unit = serializers.CharField()
    # fuel_type = serializers.CharField()
    # image = serializers.ImageField()
    car_owner = serializers.SlugRelatedField(slug_field='username',
                                             queryset=User.objects.all())

    class Meta:
        model = Car
        fields = '__all__'
