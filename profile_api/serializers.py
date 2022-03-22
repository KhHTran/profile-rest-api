from rest_framework import serializers


class SampleSerializer(serializers.Serializer):
    """Sample serializer: a name field for testing Sample Api View"""
    
    name = serializers.CharField(max_length=50)
    