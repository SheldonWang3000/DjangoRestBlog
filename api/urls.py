from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    api_root,
    PostListViewSet,
    PostDetailViewSet,
    PostCreateViewSet,
    CommentBlogListViewSet,
)

app_name = 'api'
urlpatterns = [
    path('', api_root, name='post-root'),
    path('list/', PostListViewSet.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailViewSet.as_view(), name='post-detail'),
    path('posts/', PostCreateViewSet.as_view(), name='post-create'),
    path('comments/<int:blog>/', CommentBlogListViewSet.as_view(), name='comment-blog-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)