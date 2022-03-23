from xml.sax.handler import feature_external_ges
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profile_api import serializers
from rest_framework import viewsets


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


class SampleViewSet(viewsets.ViewSet):
    """Test ViewSet"""

    serializer_class = serializers.SampleSerializer

    def list(self, request):
        """Return a hello message"""
        
        viewset_features = [
            'Uses action (list, create, retrieve, update, partial_update, destroy)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]
        return Response({'message':'Hello!', 'view_set':viewset_features})
    
    def create(self, request):
        """Create a new hello message"""
        
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            msg = 'Hello {}!'.format(name)
            return Response({'message':msg})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        """Handle getting an object by its id"""
        return Response({'HTTP Method':'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'HTTP Method':'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'HTTP Method':'PATCH'})

    def destroy(self, request, pk=None):
        """Handle destroy an object"""
        return Response({'HTTP Method':'DELETE'})