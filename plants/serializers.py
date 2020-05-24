from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Category, Plant, Room, UserPlant

class AdminCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'description',
            'slug',
            'user',
            'image_url',
            "url",
        ]
        Lookup_field = 'slug'
        extra_kwargs = {"url": {"lookup_field":"slug"}}


class CategorySerializer(AdminCategorySerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    
    
class AdminPlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'description',
            'slug',
            'user',
            'image_url',
            "url",
        ]
        Lookup_field = 'slug'
        extra_kwargs = {"url": {"lookup_field":"slug"}}

class PlantSerializer(AdminPlantSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = Plant
        fields = [
            'id',
            'name',
            'description',
            'category',
            'water_interval',
            'fertilizing_interval',
            'required_humidity',
            'required_temperature',
            'blooming',
            'difficulty',
            'user',
            "url",
        ]
class AdminRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'description',
            'slug',
            'user',
            'image_url',
            "url",
        ]
        Lookup_field = 'slug'
        extra_kwargs = {"url": {"lookup_field":"slug"}}



class RoomSerializer(AdminRoomSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = Room
        fields = [
            'id',
            'name',
            'description',
            'exposure',
            'humidity',
            'temperature',
            'drafty',
            'user',
            'url',
        ]

class AdminUserPlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'description',
            'slug',
            'user',
            'image_url',
            "url",
        ]
        Lookup_field = 'slug'
        extra_kwargs = {"url": {"lookup_field":"slug"}}        

class UserPlantSerializer(AdminUserPlantSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = UserPlant
        fields = [
            'id',
            'name',
            'description',
            'room',
            'plant',
            'last_watered',
            'last_fertilized',
            'image_url',
            'user',
            "url",
        ]


class UserSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "username",
            "email",
            "password",
        ]