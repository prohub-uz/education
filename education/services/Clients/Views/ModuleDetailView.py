from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from education.models import Module
from education.services.Clients.Serializers.GetModulesSerializer import GetModuleSerializer

class ModuleDetailView(APIView):
    def get(self, request, pk):
        module = Module.objects.get(id=pk)
        serializer = GetModuleSerializer(module, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)