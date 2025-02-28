from education.services.Serializers.GetCategorySerializer import GetCategorySerializer
from education.models import Category
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class GetListCategories(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer = GetCategorySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    