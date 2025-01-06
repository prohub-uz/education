from education.services.Serializers.GetLessonSerializer import LessonSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from education.models import Lesson
from education.models import Module


# Filter list of Lessons by Module
class GetLessonsListView(APIView):
    def get(self, request):
        lessons = Lesson.objects.all()
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)