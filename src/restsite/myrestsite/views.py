from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status
from . import permissions
from rest_framework.authentication import TokenAuthentication
from . import models
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
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

class HelloViewSet(viewsets.ViewSet):
    """test api viewset"""
    def list(self,request):
        """hello meessage"""
        a_viewset=[
            'uses actions(list,create,update,insert,destroy)',
            'Automatically maps to urls using routers',
            'provides more functionality with less code',
        ]
        return Response({'message':'hello','a_viewset':a_viewset})


class UserProfileViewSet(viewsets.ModelViewSet):
    """handles creating updating"""
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
    filter_backends=(filters.SearchFilter,)
    search_fields=('name','email',)

class LoginViewSet(viewsets.ViewSet):
    """checks email and password and validate"""
    serializer_class=AuthTokenSerializer
    
    def create(self,request):
        """use ObtainAuthToken APIVIEW to obtain and create a token"""
        return ObtainAuthToken().post(request)

class ProfileFeedItemViewSet(viewsets.ModelViewSet):
    serializer_class=serializers.ProfileFeedItemSerializer
    queryset=models.ProfileFeedItem.objects.all()
    authentication_classes=[TokenAuthentication,]

    def perform_create(self,serializer):
        """sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)