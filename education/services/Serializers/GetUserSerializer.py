from rest_framework import serializers
from education.models import User

class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name')