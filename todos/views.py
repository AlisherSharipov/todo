from django.shortcuts import render
from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer

class ListTodo(generics.ListAPIView):#list
	queryset = Todo.objects.all()
	serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveAPIView):#detail
	queryset = Todo.objects.all()
	serializer_class = TodoSerializer