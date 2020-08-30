from rest_framework import serializers
from articles.models import Article,Comment
from users.models import CustomUser

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Article
        fields=("id","title","auther","body")

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields = ('id', 'article', 'comment', 'author')  


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=('id','username','email','password')           