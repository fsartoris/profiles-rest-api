from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """test api view"""

    def get(self, request, format=None):
        """return list api features"""
        an_apiview = [
            'Uses HTTP methods as function',
            'similar to traditional django view',
            'gives control app logic',
            'map manually to url',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
