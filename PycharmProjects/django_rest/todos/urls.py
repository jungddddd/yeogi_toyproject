# todo/urls.py

from django.urls import path
from .views import TodoCreateAPIView, TodoUpdateAPIView, TodoListAPIView

urlpatterns = [
    path('todos/', TodoListAPIView.as_view(), name='todo-list'),  # 전체 조회 추가
    path('todos/create/<int:id>/', TodoCreateAPIView.as_view(), name='todo-create'),
    path('todos/update/<int:id>/', TodoUpdateAPIView.as_view(), name='todo-update')
]