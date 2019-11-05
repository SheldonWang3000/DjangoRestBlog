from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    api_root,
    PostListViewSet,
    PostDetailViewSet,
    PostCreateViewSet,
)

app_name = 'api'
urlpatterns = [
    path('', api_root, name='post-root'),
    path('list/', PostListViewSet.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailViewSet.as_view(), name='post-detail'),
    path('posts/', PostCreateViewSet.as_view(), name='post-create')
]

urlpatterns = format_suffix_patterns(urlpatterns)