from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegistrationSerializer
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


class UserRegisterView(APIView):

    def post(self, request):
        ser_data = RegistrationSerializer(data=request.data)
        if ser_data.is_valid():
            user = ser_data.save()

            refresh = RefreshToken.for_user(user)
            access = refresh.access_token

            return Response({
                'user': ser_data.data,
                'refresh_token': str(refresh),
                'access_token':str(access),
            }, status=status.HTTP_201_CREATED)
        
        return Response(data=ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self, request):

        refresh = request.data.get('refresh')
        if not refresh:
            return Response({'error':'Refresh token is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            token = RefreshToken(refresh)
            token.blacklist()
            return Response({'detail':'Logged out successful'}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as err:
            return Response({'error':str(err)}, status=status.HTTP_400_BAD_REQUEST)