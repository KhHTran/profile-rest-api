from xml.sax.handler import feature_external_ges
from rest_framework.views import APIView
from rest_framework.response import Response


class SampleAPIView(APIView):
    """Sample API View"""
    
    def get(self, request, format=None):
        """Returns a list of APIView features"""

        feature = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Similar to Django traditional view',
            'Give maximum control over application logic',
            'Mapped manually to URLs'
        ]
        return Response({
            'message': 'sample api view',
            'feature': feature
        })