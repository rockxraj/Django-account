from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Account
   
class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(max_length=100, required=True)
    last_name = serializers.CharField(max_length=100, required=True)     
    class Meta:
        model = User
        fields = ('username','password', 'first_name', 'last_name')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
        
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        #fields = ('id','title')
        fields = '__all__'
