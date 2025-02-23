from education.services.Serializers.GetListSpecialitiesSerializer import ListSpecialitiesSerializer
from education.models import Speciality
from rest_framework.response import Response
from rest_framework import status
from education.models import Speciality
from rest_framework.views import APIView

# Get speciality by id
class GetSpecialityDetailView(APIView):
    def get(self, request, pk):
        speciality = Speciality.objects.get(id=pk)
        serializer = ListSpecialitiesSerializer(speciality, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)