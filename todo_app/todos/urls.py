from django.urls import path
from .views import ListTodo, DetailTodo, UpdateTodo, DeleteTodo, CreateTodo


urlpatterns = [
    path('<int:pk>/', DetailTodo.as_view()),
    path('', ListTodo.as_view()),
    path('create', CreateTodo.as_view()),
    path('update/<int:pk>', UpdateTodo.as_view()),
    path('delete/<int:pk>', DeleteTodo.as_view())
]