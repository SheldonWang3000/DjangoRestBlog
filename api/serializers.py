from posts.models import Post 
from rest_framework import serializers
from .globalFunc import markdown2Abstract

class PostCreateSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    publish_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    abstract = serializers.ReadOnlyField()
    class Meta:
        model = Post
        fields = [
            'url',
            'user',
            'title',
            'content',
            'abstract',
            'publish_date',
        ]
        extra_kwargs = {
            'url': {'view_name': 'api_v1:post-detail'},
        }

    def create(self, validated_data):
        return Post.objects.create(**validated_data, abstract=markdown2Abstract(validated_data['content']))

    

class PostListSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    publish_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    class Meta:
        model = Post
        fields = [
            'id',
            'url',
            'user',
            'abstract',
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