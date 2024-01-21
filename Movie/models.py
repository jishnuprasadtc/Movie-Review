from django.db import models

from django.contrib.auth.models import User


# Create your models here.

class Gener(models.Model):
    name=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to="images")
    description=models.CharField(max_length=300)
    gener=models.ForeignKey(Gener,on_delete=models.CASCADE)
    director=models.CharField(max_length=200)
    cast=models.CharField(max_length=200)
    language=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    is_trending=models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Review(models.Model):
    movies=models.ForeignKey(Movie,on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)

   

