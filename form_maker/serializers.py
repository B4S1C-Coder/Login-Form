from rest_framework import serializers
from .models import FormMetaData

# class HTMLContentSerializer(serializers.Serializer):
#     content = serializers.CharField()

class FormMetaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormMetaData
        fields = ['user', 'background_image', 'logo_image', 'specific_questions_json']