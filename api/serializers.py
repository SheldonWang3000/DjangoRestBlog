from posts.models import Post 
from comments.models import Comment
from rest_framework import serializers
from .globalFunc import markdown2Abstract
from django.urls import reverse


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'blog',
            'content',
            'parent',
            'avatar',
            'username',
        ]
    def validate(self, data):
        """
        Check that the parent belongs to the same blog 
        """
        if data['parent'] is not None and data['parent'].blog.id != data['blog'].id:
            raise serializers.ValidationError("parent comment does not belong to the same blog")
        return data

class CommentListSerializer(serializers.ModelSerializer):
    parent_comment = serializers.SerializerMethodField()
    publish_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    class Meta:
        model = Comment
        fields = [
            'id',
            'content',
            'avatar',
            'username',
            'publish_date',
            'parent_comment',
        ]
    def get_parent_comment(self, obj):
        if obj.parent is not None:
            return CommentListSerializer(Comment.objects.get(pk=obj.parent_id)).data
        else:
            return None


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
    # comments = serializers.HyperlinkedIdentityField(view_name='api_v1:comment-blog-list', lookup_field='id', lookup_url_kwarg='blog')
    comments = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            'user', 
            'title', 
            'content', 
            'comments',
            'publish_date', 
            'modified_date', 
            'viewed_times',
            ]

    def get_comments(self, obj):
        if len(Comment.objects.filter(blog=obj.id)) == 0:
            return None
        else:
            return (self.context['request'].build_absolute_uri(reverse('api_v1:comment-blog-list', kwargs={'blog': obj.id})))
        return None