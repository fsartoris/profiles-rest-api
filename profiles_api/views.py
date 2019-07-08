from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """test api view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """return list api features"""
        an_apiview = [
            'Uses HTTP methods as function',
            'similar to traditional django view',
            'gives control app logic',
            'map manually to url',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})


    def post(self, request):
        """create hello messages"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


    def put(self, request, pk=None):
        """handle update object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """handle patch request"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """handle delete request"""
        return Response({'method': 'DELETE'})
