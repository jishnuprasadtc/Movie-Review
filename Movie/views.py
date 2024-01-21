from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet,ViewSet
from rest_framework import authentication
from rest_framework import permissions 
from rest_framework.decorators import action

from Movie.serializers import UserSerializer,MovieSerializer,MovieReviewserializer
from Movie.models import Movie,Review

# Create your views here.


class SignUpview(APIView):
    def post(self,request,*args,**kwargs):
        serializers=UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data)
        else:
            return Response(data=serializers.errors)
        

class MovieView(ModelViewSet):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    @action(methods=["post"],detail=True)
    def review_add(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Movie_obj=Movie.objects.get(id=id)
        serialiser=MovieReviewserializer(data=request.data)
        if serialiser.is_valid():
            serialiser.save(movies=Movie_obj,user=request.user)
            return Response(data=serialiser.data)
        else:
            return Response(data=serialiser.errors)
        
    @action(methods=["get"],detail=True)
    def review_list(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Review.objects.filter(movies=id)
        serializer=MovieReviewserializer(qs,many=True)
        return Response(data=serializer.data)
    



        
    