from posts.models import Post
from comments.models import Comment
from django.utils import timezone

from rest_framework.filters import SearchFilter
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    DestroyAPIView,
    ListAPIView,
    CreateAPIView,
    )
from api.serializers import (
    PostDetailSerializer,
    PostListSerializer,
    PostCreateSerializer,
    CommentListSerializer,
    CommentSerializer,
    )
from .globalFunc import markdown2Abstract

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'list': reverse('api_v1:post-list', request=request, format=format),
        'create': reverse('api_v1:post-create', request=request, format=format)
    })

class CommentBlogListViewSet(ListAPIView):
    serializer_class = CommentListSerializer
    def get_queryset(self):
        blog_id = self.kwargs['blog']
        queryset = Comment.objects.filter(blog_id=blog_id)
        return queryset.order_by('-publish_date')

class CommentDeleteViewSet(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentCreateViewSet(CreateAPIView):
    serializer_class = CommentSerializer

class PostCreateViewSet(CreateAPIView):
    serializer_class = PostCreateSerializer

class PostListViewSet(ListAPIView):
    queryset = Post.objects.all().order_by('-modified_date')
    serializer_class = PostListSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'content']

class PostDetailViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

    def put(self, request, *args, **kwargs):
        obj = self.get_object()
        new_obj = request.data
        if (obj.content is not new_obj['content']) or (obj.title is not new_obj['title']):
            obj.modified_date = timezone.now()
            if (obj.content is not new_obj['content']):
                obj.abstract = markdown2Abstract(new_obj['content'])
            obj.save()
        return super(PostDetailViewSet, self).update(request, args, kwargs)


    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.viewed_times += 1
        instance.save()
        return Response(PostDetailSerializer(instance, context={'request':request}).data)
