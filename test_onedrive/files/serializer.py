# coding: utf-8

from rest_framework import serializers

from .models import File, TempFile


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('name', 'fileId', 'pub_date')

class TempFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempFile
        fields = ('file')