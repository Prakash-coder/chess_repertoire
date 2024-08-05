from .models import YourOpening
from rest_framework import status
from .serializers import YourOpeningSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class OpeningList(APIView):
    def get(self, request):
        openings = YourOpening.objects.all()
        serializer = YourOpeningSerializer(openings, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = YourOpeningSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OpeningDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(YourOpening, pk=pk)

    def get(self, request, pk):
        opening = self.get_object(pk)
        serializer = YourOpeningSerializer(opening)
        return Response(serializer.data)
    
    def put(self, request, pk):
        opening = self.get_object(pk)
        serializer = YourOpeningSerializer(opening, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        opening = self.get_object(pk)
        opening.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
