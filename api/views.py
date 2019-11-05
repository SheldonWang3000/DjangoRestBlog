from posts.models import Post
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, 
    ListAPIView, 
    CreateAPIView,
    )
from api.serializers import (
    PostDetailSerializer, 
    PostListSerializer,
    PostCreateSerializer,
    )

class PostCreateViewSet(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostListViewSet(ListAPIView):
    queryset = Post.objects.all().order_by('-publish_date')
    serializer_class = PostListSerializer

class PostDetailViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    def put(self, request, *args, **kwargs):
        obj = self.get_object()
        new_obj = request.data
        if (obj.content is not new_obj['content']) or (obj.title is not new_obj['title']):
            obj.modified_date = timezone.now()
            obj.save()
        return super(PostDetailViewSet, self).update(request, args, kwargs)


    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.viewed_times += 1
        instance.save()
        return Response(PostDetailSerializer(instance).data)

