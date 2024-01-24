from rest_framework import status
from rest_framework import generics
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from . models import User
from . serializers import MyTokenObtainPairSerializer, MyUserSerializer

class MyTokenObtainPairSerializer(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
@api_view(['POST'])
def register(request):
    data = request.data
    try:
        user = User.objects.create(
            username=data['username'],
            email=data['email'],
            password=make_password(data['password'])
        )
        serializer = MyUserSerializer(user, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'something went wrong'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
        