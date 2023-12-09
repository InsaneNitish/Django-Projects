from django.shortcuts import render
from fvbApp.models import *
from fvbApp.serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
@api_view(['GET','POST'])
def student_list(request):
    if request.method=='GET':
        student=Student.objects.all()
        serializer=StudentSerializer(student,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
# Create your views here.
