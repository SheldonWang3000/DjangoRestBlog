from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    api_root,
    PostListViewSet,
    PostDetailViewSet,
    PostCreateViewSet,
    CommentBlogListViewSet,
    CommentDeleteViewSet,
    CommentCreateViewSet,
)

app_name = 'api'
urlpatterns = [
    path('', api_root, name='post-root'),
    path('list/', PostListViewSet.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailViewSet.as_view(), name='post-detail'),
    path('posts/', PostCreateViewSet.as_view(), name='post-create'),
    path('comments/create/', CommentCreateViewSet.as_view(), name='comment-create'),
    path('comments/blog/<int:blog>/', CommentBlogListViewSet.as_view(), name='comment-blog-list'),
    path('comments/<int:pk>/', CommentDeleteViewSet.as_view(), name='comment-delete')
]

urlpatterns = format_suffix_patterns(urlpatterns)