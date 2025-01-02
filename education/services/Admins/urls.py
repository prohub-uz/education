from django.urls import path, include
from rest_framework import routers
from .Views.ManageEducation import ManageSpeciality, ManageModule, ManageLesson

router = routers.DefaultRouter()
router.register('control-speciality', ManageSpeciality)
router.register('control-module', ManageModule)
router.register('control-lesson', ManageLesson)

urlpatterns = [
    path('', include(router.urls)),
]
