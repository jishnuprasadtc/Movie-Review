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
    gener=models.ManyToManyField(Gener)
    director=models.CharField(max_length=200)
    cast=models.CharField(max_length=200)
    language=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    is_trending=models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    # all review
    @property
    def movie_rew(self):
        qs=self.review.all()
        return qs
    
    #  review_count from all review
    @property
    def Review_count(self):
        qs=self.movie_rew
        return len(qs)

    #  total average
    @property
    def total_avg(self):
        movie_reviews=self.movie_rew
        review_count=self.Review_count
        avg=0
        if movie_reviews:
            total_rating=sum([mrv.rate for mrv in movie_reviews])
            avg=total_rating//review_count
        return avg

            
       

    #  mive_reviews=movifdtujdhg
    #  review_count=
    #  total=moviews_reviews.rayting
    # avg= total//(review_cxount)


class Review(models.Model):
    movies=models.ForeignKey(Movie,on_delete=models.CASCADE,null=True,related_name="review")
    comment=models.CharField(max_length=200)
    option=((1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10),)
    rate=models.PositiveIntegerField(choices=option,default=5)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)

   

