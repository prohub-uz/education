from rest_framework import serializers
from education.models import Lesson
from education.services.Clients.Serializers.GetModulesSerializer import GetModuleSerializer
from education.services.Clients.Serializers.GetListSpecialitiesSerializer import ListSpecialitiesSerializer

# Get lessons by module
class LessonSerializer(serializers.ModelSerializer):
    module = GetModuleSerializer()
    class Meta:
        model = Lesson
        fields = '__all__'
        