from education.services.Serializers.GetModulesSerializer import GetModuleSerializer
from education.models import Module
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


# Get modules by speciality
class GetModules(APIView):
    def get(self, request):
        module = Module.objects.all()
        serializer = GetModuleSerializer(module, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
