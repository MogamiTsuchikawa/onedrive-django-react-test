from django.shortcuts import render
import django_filters
from rest_framework import viewsets, filters
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import status

from .models import File,TempFile
from .serializer import FileSerializer,TempFileSerializer

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

class TempFileViewSet(viewsets.ViewSet):
    parser_class = (FileUploadParser,)

    def create(self, request):
        context = {
            "request": self.request,
        }
        serializer = TempFileSerializer(data=request.data, context=context)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)