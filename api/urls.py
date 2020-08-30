from django.urls import path
from .views import NewsAPIView,NewsAPIView1,CommentsAPIView,CommentsAPIView1,UsersAPIView,UsersAPIView1


urlpatterns = [
    
    path("users/<int:pk>/",UsersAPIView1.as_view()),
    path("users/",UsersAPIView.as_view()),
    path("comments/<int:pk>/",CommentsAPIView1.as_view()),
    path("comments/",CommentsAPIView.as_view()),
    path("<int:pk>/",NewsAPIView1.as_view()),
    path("",NewsAPIView.as_view()),
]
