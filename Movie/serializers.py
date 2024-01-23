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
    

class MovieReviewserializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField()
    movies=serializers.StringRelatedField()
    class Meta:
        model=Review
        fields="__all__"
        read_only_fields=["id","movies","user","created_at","updated_at","is_active"]


class MovieSerializer(serializers.ModelSerializer):
    gener=serializers.StringRelatedField(many=True)
    movie_rew=MovieReviewserializer(read_only=True,many=True)
    total_avg=serializers.CharField(read_only=True)
    class Meta:
        model=Movie
        fields=["id","name","image","description","gener","director","cast","language","created_at","updated_at","is_active","is_trending","movie_rew","total_avg"]
