from rest_framework import serializers
from education.models import Speciality
from education.services.Serializers.GetTeacherSerializer import GetTeacherSerializer
from education.services.Serializers.GetCategorySerializer import GetCategorySerializer

class ListSpecialitiesSerializer(serializers.ModelSerializer):
    teacher = GetTeacherSerializer()
    category = GetCategorySerializer()
    class Meta:
        model = Speciality
        fields = '__all__'