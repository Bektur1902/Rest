
from rest_framework import serializers
from .models import *


class CarListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'vin', 'brand')


class CarDetailSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Car
        fields = '__all__'