from xml.sax.handler import feature_external_ges
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profile_api import serializers


class SampleAPIView(APIView):
    """Sample API View"""
    
    serializer_class = serializers.SampleSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        feature = [
            'Uses HTTP methods as function ' \
            '(get, post, patch, put, delete)',
            'Similar to Django traditional view',
            'Give maximum control over application logic',
            'Mapped manually to URLs'
        ]
        return Response({
            'message':'sample api view',
            'feature':feature
        })

    def post(self, request, format=None):
        """Create greeting message with name received"""
        
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = 'Hello {}'.format(name)
            return Response({'message':message})
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
        )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method':'PATCH'})
    
    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})