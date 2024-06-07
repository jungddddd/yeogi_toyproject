# todo/urls.py

from django.urls import path
from .views import TodoListAPIView, TodoDestroyAPIView, TodoListRetrieveAPIView

urlpatterns = [
    path('todos/list', TodoListAPIView.as_view(), name='todo-list-retrieve'),  # 변경된 URL 패턴 이름
    path('todos/list/<int:id>/', TodoListRetrieveAPIView.as_view(), name='todo-detail'),
    path('todos/delete/<int:id>/', TodoDestroyAPIView.as_view(), name='todo-delete'),
]
