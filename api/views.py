from posts.models import Post
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from api.serializers import PostDetailSerializer, PostListSerializer

class PostListViewSet(ListAPIView):
    queryset = Post.objects.all().order_by('publish_date')
    serializer_class = PostListSerializer

class PostDetailViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    def put(self, request, *args, **kwargs):
        obj = self.get_object()
        new_obj = request.data
        print(obj.content)
        print(new_obj['content'])
        print(obj.title)
        print(new_obj['title'])
        if (obj.content is not new_obj['content']) or (obj.title is not new_obj['title']):
            obj.modified_date = timezone.now()
            obj.save()
            print(obj.modified_date)
        return super(PostDetailViewSet, self).update(request, args, kwargs)


    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.viewed_times += 1
        instance.save()
        return Response(PostDetailSerializer(instance).data)

