from django.urls import path

from Movie import views

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("movies",views.MovieView,basename="movies")



urlpatterns=[
    path("register/",views.SignUpview .as_view()),
    path("token/",ObtainAuthToken.as_view())

]+router.urls