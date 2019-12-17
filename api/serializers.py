from posts.models import Post 
from comments.models import Comment
from deleteList.models import (DeleteTransaction, DeleteArray)

from rest_framework import serializers
from .globalFunc import markdown2Abstract
from django.urls import reverse
from django.shortcuts import get_object_or_404

class DeleteTransactionSerializer(serializers.HyperlinkedModelSerializer):
    link = serializers.HyperlinkedIdentityField(view_name='api_v1:delete-execute', 
        lookup_url_kwarg='transaction',
        lookup_field='id'
        )
    array = serializers.ListField(child=serializers.IntegerField(), write_only=True)
    class Meta:
        model = DeleteTransaction
        fields = [
            'link',
            'array'
        ]
    def create(self, validated_data):
        l = validated_data.pop('array')
        obj = DeleteTransaction.objects.create(**validated_data)
        for item in l:
            DeleteArray.objects.create(transaction=obj, blog=get_object_or_404(Post, pk=item))
        return obj

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
    children_comment = serializers.SerializerMethodField()
    publish_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    class Meta:
        model = Comment
        fields = [
            'id',
            'content',
            'avatar',
            'username',
            'publish_date',
            'children_comment',
        ]
    def get_children_comment(self, obj):
        queryset = Comment.objects.filter(parent=obj.pk).order_by('-publish_date')
        if len(queryset) != 0:
            return [CommentListSerializer(item).data for item in queryset]
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


class PostDashboardListSerializer(serializers.ModelSerializer):
    publish_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    modified_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    viewed_times = serializers.IntegerField(read_only=True)
    comments_num = serializers.IntegerField(read_only=True)
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'viewed_times',
            'comments_num',
            'publish_date',
            'modified_date',
            'sticky',
        ]