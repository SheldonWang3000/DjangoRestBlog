from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    PostListViewSet,
    PostDetailViewSet
)

app_name = 'api'
urlpatterns = [
    path('list/', PostListViewSet.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailViewSet.as_view(), name='post-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)