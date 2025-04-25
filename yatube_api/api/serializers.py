from rest_framework import serializers

from posts.models import Comment, Group, Post


class CommentSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('author', 'id', 'post')


class PostSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')
    group = serializers.SlugRelatedField(slug_field='slug',
                                         queryset=Group.objects.all(),
                                         required=False)

    class Meta:
        fields = '__all__'
        model = Post
        read_only_fields = ('author', 'id')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        read_only_fields = ('id',)
        model = Group