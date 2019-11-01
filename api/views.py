from posts.models import Post
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from api.serializers import PostDetailSerializer, PostListSerializer

class PostListViewSet(ListAPIView):
    queryset = Post.objects.all().order_by('publish_date')
    serializer_class = PostListSerializer

class PostDetailViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

