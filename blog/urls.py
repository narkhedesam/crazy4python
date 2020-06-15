from django.contrib import admin
from django.urls import path, include
from .views import PostList, search_blog, PostDetails

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('search_blog/', search_blog.as_view(), name='search_blog'),
    path('<slug:slug>/', PostDetails.as_view(), name='post_detail'),
]
