from django.contrib import admin
from .models import User, Speciality, Module, Lesson

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'id')
    ordering = ['id']


@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'teacher', 'id')
    ordering = ['id']


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'speciality', 'price', 'description', 'id')
    ordering = ['id']
    

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'module', 'description', 'source', 'id')
    list_filter = ('module',)
    search_fields = ('name', 'description')
    ordering = ['id']
