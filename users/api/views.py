from rest_framework.generics import CreateAPIView
from django.db.models import Q
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.status import  HTTP_200_OK,HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

User=get_user_model()
from .serializers import (
    UserCreateSerializer,
    UserLoginSerializer
)

from rest_framework.permissions import (

    AllowAny,
    IsAuthenticated,
    IsAdminUser
)

class UserCreateAPIView(CreateAPIView):
    serializer_class=UserCreateSerializer
    queryset=User.objects.all()
class UserLoginAPIView(APIView):
    permission_classes=[AllowAny]
    serializer_class=UserLoginSerializer

    def post(self,request,*args,**kwargs):
        data=request.data
        serializer=UserLoginSerializer(data=data)
        if serializer.is_valid():
            new_data=serializer.data
            response = {
                 'result': '1'
                }
            return Response(response,status=HTTP_200_OK)
        else:   
            response1 = {
                 'result': '0'
                }
            return Response(response1,status=HTTP_400_BAD_REQUEST)


