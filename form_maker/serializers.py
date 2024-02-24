from rest_framework import serializers

class HTMLContentSerializer(serializers.Serializer):
    content = serializers.CharField()