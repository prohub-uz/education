from django.contrib import admin
from .models import User, Speciality, Module, Lesson, Teacher, Homework, Category

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'id')
    list_editable = ('email', 'first_name', 'last_name')
    ordering = ['id']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    ordering = ['id']

@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'duration', 'description', 'for_who', 'requirements', 'what_will_you_learn', 'picture', 'teacher', 'id')
    list_editable = ('teacher', 'picture', 'category')
    list_filter = ('teacher',)
    ordering = ['id']


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'speciality', 'price', 'description', 'id')
    list_editable = ('price', 'description')
    list_filter = ('speciality',)
    ordering = ['id']
    

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'module', 'description', 'source', 'id')
    list_editable = ('source', 'description', 'module')
    list_filter = ('module',)
    search_fields = ('name', 'description')
    ordering = ['id']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'about', 'is_active', 'id')
    list_editable = ('is_active', 'about')
    ordering = ['id']


@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'name', 'description', 'source', 'id')
    list_editable = ('source', 'description')
    list_filter = ('lesson',)
    ordering = ['id']