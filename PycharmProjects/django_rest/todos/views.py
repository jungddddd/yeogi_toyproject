# todo/views.py

from rest_framework import generics
from .models import TodoItem
from .serializer import TodoItemSerializer

class TodoCreateAPIView(generics.CreateAPIView): # 게시글 생성
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

class TodoUpdateAPIView(generics.UpdateAPIView): # 게시글 수정
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    lookup_field = 'id'  # lookup_field를 'id'로 설정

class TodoListAPIView(generics.ListAPIView):  # 게시글 전체 조회
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
