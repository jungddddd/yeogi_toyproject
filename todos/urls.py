# todo/urls.py

from django.urls import path
from .views import TodoListAPIView, TodoDestroyAPIView, TodoListRetrieveAPIView, TodoCreateAPIView, TodoUpdateAPIView, BoardView,TodoView, ResearchView, ReadView

urlpatterns = [
    path('todos/create/<int:id>/', TodoCreateAPIView.as_view(), name='todo-create'),
    path('todos/create/', TodoCreateAPIView.as_view(), name='todo-create'),
    path('todos/update/<int:id>/', TodoUpdateAPIView.as_view(), name='todo-update'),
    path('todos/list', TodoListAPIView.as_view(), name='todo-list-retrieve'),  # 변경된 URL 패턴 이름
    path('todos/list/<int:id>/', TodoListRetrieveAPIView.as_view(), name='todo-detail'),
    path('todos/delete/<int:id>/', TodoDestroyAPIView.as_view(), name='todo-delete'),
    path('board/', BoardView, name='board'),
    path('todo/board.html', BoardView, name='board'),
    path('todo/', TodoView, name='todo-html'),
    path('todo/todo.html', TodoView, name='todo-html'),
    path('todo/research.html', ResearchView, name='research'),  # /todo/research.html 경로 추가
    path("list_Read/", ReadView, name='read_list'),
    path('board/<int:id>/', BoardView, name='board-with-id'),  # 매개변수를 전달하는 board.html로의 경로 설정
    
]
