from rest_framework import serializers

from django.contrib.auth.models import User

from Movie.models import Movie,Review


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username","email","password"]
        read_only_fields=["id"]



    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    

class MovieSerializer(serializers.ModelSerializer):
    gener=serializers.StringRelatedField()
    class Meta:
        model=Movie
        fields="__all__"
        read_only_fields=["id"]


class MovieReviewserializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField()
    movies=serializers.StringRelatedField()
    class Meta:
        model=Review
        fields="__all__"
        read_only_fields=["id","movies","user","created_at","updated_at","is_active"]
