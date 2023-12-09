from rest_framework import serializers
from fvbApp.models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        field=['rollno','fname','lname']