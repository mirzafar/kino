from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *

class IndexView(APIView):
    def get(self, request):
        films = Film.objects.all()
        filmserializer = FilmSerializer(films, many=True) 
        return Response({"films": filmserializer.data})

