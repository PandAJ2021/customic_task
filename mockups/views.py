from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Mockup
from .serializers import MockupSerializer


class CreateMockupView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        ser_data = MockupSerializer(data=request.data, context={'request': request})
        if ser_data.is_valid():
            mockup = ser_data.save()
            
            # image generating func

            return Response({
                "task_id": str(mockup.task_id),
                "status": "PENDING",
                "message": "generating image started"
            }, status=status.HTTP_201_CREATED)
        
        return Response(data=ser_data.errors, status=status.HTTP_400_BAD_REQUEST)