from django.shortcuts import render
from rest_framework import generics
from articles.models import Article,Comment
from users.models import CustomUser
from .serializers import ArticleSerializer,CommentSerializer,UsersSerializer

# Create your views here.

class NewsAPIView(generics.ListCreateAPIView):
    queryset= Article.objects.all()
    serializer_class=ArticleSerializer
    

class NewsAPIView1(generics.RetrieveUpdateDestroyAPIView):
    queryset= Article.objects.all()
    serializer_class=ArticleSerializer

class CommentsAPIView(generics.ListCreateAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer

class CommentsAPIView1(generics.RetrieveUpdateDestroyAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer

class UsersAPIView(generics.ListCreateAPIView):
    queryset=CustomUser.objects.all()
    serializer_class=UsersSerializer

class UsersAPIView1(generics.RetrieveUpdateDestroyAPIView):
    queryset=CustomUser.objects.all()
    serializer_class=UsersSerializer
