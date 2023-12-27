from django.db import IntegrityError
from rest_framework import serializers
from .models import Follower


class FollowerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    followed_name = serializers.ReadOnlyField(source='owner.username')


    class Meta:
        model = Like
        fields = ['id', 'owner', 'created_at', 'followed', 'followed_name']


    def create(self, validated_data):
        try:
            return super().create(validated_data)  
        except:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })

