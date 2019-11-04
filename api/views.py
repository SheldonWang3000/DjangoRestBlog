from posts.models import Post
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from api.serializers import PostDetailSerializer, PostListSerializer

class PostListViewSet(ListAPIView):
    queryset = Post.objects.all().order_by('publish_date')
    serializer_class = PostListSerializer

class PostDetailViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.viewed_times += 1
        instance.save()
        return Response(PostDetailSerializer(instance).data)

