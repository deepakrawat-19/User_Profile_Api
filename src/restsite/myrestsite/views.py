from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    """test apiview"""
    def get(self,request,format=None):
        """returns list of api view feature"""

        an_apiview=[
            'uses HTTP methods as function(get,post,patch,delete,put)',
            'it is similar to traditional django view',
            'gives u the most control over the logic',
            'it is mapped usually to urls',
        ]

        return Response({'message':'helloapi','an_apiview':an_apiview})