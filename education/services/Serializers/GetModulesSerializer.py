from rest_framework import serializers
from education.models import Module
from education.services.Clients.Serializers.GetListSpecialitiesSerializer import ListSpecialitiesSerializer

# Get modules by speciality
class GetModuleSerializer(serializers.ModelSerializer):
    speciality = ListSpecialitiesSerializer()
    class Meta:
        model = Module
        fields = '__all__'
