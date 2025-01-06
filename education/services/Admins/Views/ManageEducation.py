from rest_framework.viewsets import ModelViewSet
from education.models import Speciality, Module, Lesson
from education.services.Serializers.GetListSpecialitiesSerializer import ListSpecialitiesSerializer
from education.services.Serializers.GetModulesSerializer import GetModuleSerializer
from education.services.Serializers.GetLessonSerializer import LessonSerializer
from rest_framework import permissions

# Manage Speciality
class ManageSpeciality(ModelViewSet):
    queryset = Speciality.objects.all()
    serializer_class = ListSpecialitiesSerializer
    permission_classes = [permissions.IsAdminUser]


# Manage Module
class ManageModule(ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = GetModuleSerializer
    permission_classes = [permissions.IsAdminUser]
    

# Manage Lesson
class ManageLesson(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAdminUser]