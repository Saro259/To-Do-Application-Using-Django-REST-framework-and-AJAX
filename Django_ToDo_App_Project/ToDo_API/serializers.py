from rest_framework import serializers
from .models import Task

'''The class declares which model to be serialized, in order to return a JSON object '''
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields ='__all__'