from education.services.Serializers.GetListSpecialitiesSerializer import ListSpecialitiesSerializer
from education.models import Speciality
from rest_framework.response import Response
from rest_framework import status
from education.models import Speciality
from rest_framework.views import APIView

class GetListSpecialities(APIView):
    def get(self, request):
        speciality = Speciality.objects.all()
        serializer = ListSpecialitiesSerializer(speciality, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)