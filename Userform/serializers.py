from rest_framework import serializers
from .models import Userform

class UserformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userform
        fields = '__all__'
