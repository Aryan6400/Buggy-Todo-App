from rest_framework import generics
from .serializers import TodoSerializer
from .models import Todo


class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DetailTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class CreateTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class UpdateTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DeleteTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer