from rest_framework import serializers
from reviewer.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'id',
            'guid',
            'title',
            'description',    
            'status',
        ]

class CourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'guid',
            'title',
            'description',    
            'status',
        ]
        