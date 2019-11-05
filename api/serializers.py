from posts.models import Post 
from rest_framework import serializers

class PostCreateSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    publish_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    class Meta:
        model = Post
        fields = [
            'url',
            'user',
            'title',
            'content',
            'publish_date',
        ]
        extra_kwargs = {
            'url': {'view_name': 'api_v1:post-detail'},
        }

class PostListSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    publish_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    class Meta:
        model = Post
        fields = [
            'url',
            'user',
            'title', 
            'publish_date'
            ]
        extra_kwargs = {
            'url': {'view_name': 'api_v1:post-detail'},
        }

class PostDetailSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    publish_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    modified_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    viewed_times = serializers.IntegerField(read_only=True)
    class Meta:
        model = Post
        fields = [
            'user', 
            'title', 
            'content', 
            'publish_date', 
            'modified_date', 
            'viewed_times'
            ]