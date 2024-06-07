# todo/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from .models import TodoItem
from .serializer import TodoItemSerializer

class TodoListAPIView(generics.ListAPIView): # 게시글 전체 조회
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

class TodoListRetrieveAPIView(generics.RetrieveAPIView): # 게시글 상세 조회
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    lookup_field = 'id'  # lookup_field를 'id'로 설정

class TodoDestroyAPIView(generics.DestroyAPIView): # 게시글 삭제
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    lookup_field = 'id'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        #삭제된 항목이 더 이상 조회되지 않도록 queryset을 업데이트
        self.queryset = self.filter_queryset(self.get_queryset())

        return Response(status=status.HTTP_204_NO_CONTENT)
