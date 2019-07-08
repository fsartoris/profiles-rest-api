from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """serializers a name field to testing apiview"""
    name = serializers.CharField(max_length=10);
