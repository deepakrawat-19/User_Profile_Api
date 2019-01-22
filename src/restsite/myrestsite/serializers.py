from rest_framework import serializers
from . import models

class HelloSerializer(serializers.Serializer):
    """serializes a name field for testing our apiview"""
    name=serializers.CharField(max_length=20)

class UserProfileSerializer(serializers.ModelSerializer):
    """serializes model object"""

    class Meta:
        model=models.UserProfile
        fields=['id','name','email','password']
        extra_kwargs={'password':{'write_only':True}}

    def create(self,validatedata):
        """create and return user"""
        user=models.UserProfile(email=validatedata['email'],name=validatedata['name'])
        user.set_password(validatedata['password'])
        user.save()
        return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.ProfileFeedItem
        fields=['id','user_profile','status_text','created_on']
        extra_kwargs={'user_profile':{'write_only':True}}
