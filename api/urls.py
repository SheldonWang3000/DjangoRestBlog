from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    api_root,
    PostListViewSet,
    PostDetailViewSet,
    PostCreateViewSet,
    PostDashboardListViewSet,
    CommentBlogListViewSet,
    CommentDeleteViewSet,
    CommentCreateViewSet,
    DeleteTransactionCreateViewSet,
    DeleteTransactionExecuteViewSet,
)

app_name = 'api'
urlpatterns = [
    path('', api_root, name='post-root'),
    path('deleteList/', DeleteTransactionCreateViewSet.as_view(), name='delete-create-list'),
    path('deleteList/execute/<int:transaction>/', DeleteTransactionExecuteViewSet.as_view(), name='delete-execute'),
    path('list/', PostListViewSet.as_view(), name='post-list'),
    path('dashboard/list/', PostDashboardListViewSet.as_view(), name='post-dashboard-list'),
    path('posts/<int:pk>/', PostDetailViewSet.as_view(), name='post-detail'),
    path('posts/', PostCreateViewSet.as_view(), name='post-create'),
    path('comments/create/', CommentCreateViewSet.as_view(), name='comment-create'),
    path('comments/blog/<int:blog>/', CommentBlogListViewSet.as_view(), name='comment-blog-list'),
    path('comments/<int:pk>/', CommentDeleteViewSet.as_view(), name='comment-delete')
]

urlpatterns = format_suffix_patterns(urlpatterns)