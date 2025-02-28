from rest_framework import serializers
from education.models import Category


class GetCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'