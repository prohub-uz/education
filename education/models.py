from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator


class User(AbstractUser):
    pass
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher')
    is_active = models.BooleanField(default=True)
    about = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.user.username


class Speciality(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    is_active = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    picture = models.URLField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'Speciality'
        verbose_name_plural = 'Specialities'
    
    def __str__(self):
        return self.name


class Module(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    price = models.FloatField(validators=[MinValueValidator(0)])
    description = models.TextField(null=True, blank=True)
    
    
    class Meta:
        verbose_name = 'Module'
        verbose_name_plural = 'Modules'
    
    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    source = models.URLField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'
    
    def __str__(self):
        return self.name


class Homework(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    source = models.URLField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'Homework'
        verbose_name_plural = 'Homeworks'
    
    def __str__(self):
        return self.name