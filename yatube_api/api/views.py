from rest_framework import viewsets

from posts.models import Group, Post, Comment
from .serializers import CommentSerializer, GroupSerializer, PostSerializer



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    #Чтобы данные поста мог изменять только автор
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        

class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    #Получаем список всех комментариев поста с id= postid
    def get_queryset(self):
        post = Post.objects.get(pk=self.kwargs.get('post_id'))
        return post.comments

    #Получаем, редактируем или удаляем комментарий с id =postid
    def perform_create(self, serializer):
        post = Post.objects.get(pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)