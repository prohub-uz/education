from rest_framework import serializers
from education.models import Speciality

class ListSpecialitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = '__all__'