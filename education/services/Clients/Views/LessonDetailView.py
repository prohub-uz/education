from education.models import Lesson
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from education.services.Clients.Serializers.GetLessonSerializer import LessonSerializer

class LessonDetailView(APIView):
    def get(self, request, pk):
        lesson = Lesson.objects.get(id=pk)
        serializer = LessonSerializer(lesson, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)