from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .models import Data
from .serializer import Dataserializer
from rest_framework import generics, status


class DataView(APIView):
    def post(self, request):
        serializer = Dataserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            
        

