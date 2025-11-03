from django.urls import path
from . import views

app_name = 'mockups'
urlpatterns = [
    path('generate/', views.CreateMockupView.as_view(), name='generate_image'),
    path('tasks/<str:task_id>/', views.TaskResultView.as_view(), name='task_result'),
    path('', views.MockupHistoryView.as_view(), name='mockups_history'),
]