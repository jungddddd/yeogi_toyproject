# todo/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from .models import TodoItem
from .serializer import TodoItemSerializer
from django.shortcuts import render

def BoardView(request):
    return render(request, 'board.html')

def TodoView(request):
    return render(request, 'todo.html')

def ResearchView(request):
    return render(request, 'research.html') 

def ReadView(request):
    return render(request, 'list_Read.html') 

class TodoCreateAPIView(generics.CreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

class TodoUpdateAPIView(generics.UpdateAPIView): # 게시글 수정
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    lookup_field = 'id'  # lookup_field를 'id'로 설정

class TodoListAPIView(generics.ListAPIView): # 게시글 전체 조회
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

class TodoListRetrieveAPIView(generics.RetrieveAPIView): # 게시글 상세 조회
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    lookup_field = 'id'  # lookup_field를 'id'로 설정

class TodoDestroyAPIView(generics.RetrieveDestroyAPIView): # 게시글 삭제
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    lookup_field = 'id'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        #삭제된 항목이 더 이상 조회되지 않도록 queryset을 업데이트
        self.queryset = self.filter_queryset(self.get_queryset())

        return Response({"message": "삭제가 성공적으로 이루어졌습니다."}, status=status.HTTP_204_NO_CONTENT)
