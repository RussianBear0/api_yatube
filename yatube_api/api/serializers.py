from rest_framework import serializers

from posts.models import Group, Post, Comment


#Сериализатор для комментариев
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

#Сериализатор для групп
class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'

#Сериализатор для поста
class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    group = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ('__all__')
