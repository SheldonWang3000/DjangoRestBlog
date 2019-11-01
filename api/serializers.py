from posts.models import Post 
from rest_framework import serializers


class PostListSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
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
    class Meta:
        model = Post
        fields = [
            'id', 
            'user', 
            'title', 
            'content', 
            'publish_date', 
            'modified_date', 
            'viewed_times'
            ]