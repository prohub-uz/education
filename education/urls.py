from django.urls import path
from .views import GetListSpecialities, GetModules, ModuleDetailView, GetLessonsListView, LessonDetailView

urlpatterns = [
    path('specialities/', GetListSpecialities),
    path('modules/', GetModules),
    path('modules/<int:pk>/', ModuleDetailView),
    path('lessons/', GetLessonsListView),
    path('lessons/<int:pk>/', LessonDetailView),
]
