from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from celery.result import AsyncResult
from core.celery import app
from .models import Result
from .serializers import MockupSerializer, ResultSerializer
from .tasks import generate_mockup_images_task
from .pagination import ResultPagination


class CreateMockupView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        ser_data = MockupSerializer(data=request.data, context={'request': request})
        if ser_data.is_valid():
            mockup = ser_data.save()
            
            task = generate_mockup_images_task.delay(mockup.id)
            task_status = AsyncResult(task.id, app=app).status

            return Response({
                "task_id":str(task.id),
                "status": task_status,
                "message": "generating image started"
            }, status=status.HTTP_201_CREATED)
        
        return Response(data=ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskResultView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, task_id):
        task_result = AsyncResult(task_id, app=app)
        task_status = task_result.status

        response_data = {
            "task_id": str(task_id),
            "status": task_status,
            "results": [],
            "error": None,
        }

        if not task_result.ready():
            return Response(response_data, status=status.HTTP_200_OK)

        if task_status == "SUCCESS":
            task_data = task_result.result
            response_data["results"] = task_data["results"]
            return Response(response_data, status=status.HTTP_200_OK)

        if task_status == "FAILURE":
            response_data["error"] = str(task_result.result)
            return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(response_data, status=status.HTTP_200_OK)
    

class MockupHistoryView(ListAPIView):
    serializer_class = ResultSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = ResultPagination

    def get_queryset(self):
        user = self.request.user
        return Result.objects.filter(mockup__user = user).select_related('mockup').order_by('-created_at')