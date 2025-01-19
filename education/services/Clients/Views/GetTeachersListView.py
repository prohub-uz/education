from rest_framework.views import APIView
from education.services.Serializers.GetTeacherSerializer import GetTeacherSerializer
from rest_framework.response import Response
from rest_framework import status
from education.models import Teacher


class GetTeachersListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = GetTeacherSerializer(teachers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)