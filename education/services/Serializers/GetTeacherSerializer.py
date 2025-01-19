from rest_framework import serializers
from education.models import Teacher
from education.services.Serializers.GetUserSerializer import GetUserSerializer


class GetTeacherSerializer(serializers.ModelSerializer):
    user = GetUserSerializer()
    class Meta:
        model = Teacher
        fields = '__all__'