from rest_framework import serializers
from education.models import Speciality
from education.services.Serializers.GetTeacherSerializer import GetTeacherSerializer

class ListSpecialitiesSerializer(serializers.ModelSerializer):
    teacher = GetTeacherSerializer()
    class Meta:
        model = Speciality
        fields = '__all__'