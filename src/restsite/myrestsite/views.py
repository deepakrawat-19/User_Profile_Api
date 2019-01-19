from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status

# Create your views here.
class HelloApiView(APIView):
    """test apiview"""
    serializer_class=serializers.HelloSerializer #serializer class object 
    def get(self,request,format=None):
        """returns list of api view feature"""
 
        an_apiview=[
            'uses HTTP methods as function(get,post,patch,delete,put)',
            'it is similar to traditional django view',
            'gives u the most control over the logic',
            'it is mapped usually to urls',
        ]

        return Response({'message':'helloapi','an_apiview':an_apiview})

    def post(self, request):
        """create a hello message with our name"""

        serializer=serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name=serializer.data.get('name')
            message='hello {0}'.format(name) #string format1
            return Response({'message':message})

        else:
            return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST) #bad request of http

    def put(self,request,pk=None):
        """handles updating object"""
        return Response({'method':'put'})

    def patch(self,request,pk=None):
        """handles patch request,updating fields provided in the request."""
        return Response({'method':'patch'})
    def delete(self,request,pk=None):
        """delete objects"""
        return Response({'method':'delete'})