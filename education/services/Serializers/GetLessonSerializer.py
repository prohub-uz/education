from rest_framework import serializers
from education.models import Lesson
from education.services.Serializers.GetModulesSerializer import GetModuleSerializer

# Get lessons by module
class LessonSerializer(serializers.ModelSerializer):
    module = GetModuleSerializer()
    class Meta:
        model = Lesson
        fields = '__all__'
        