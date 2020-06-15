from django.shortcuts import render
from django.views import generic
from django.db.models import Q
from .models import post

# Create your views here.

class PostList(generic.ListView):
    paginate_by = 10
    queryset = post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class search_blog(generic.ListView):
    # model = post
    template_name = 'search_blog.html'
    context_object_name = 'object_list'
    paginate_by = 1

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = None
        if query:
            print(query)
            object_list = post.objects.filter(
                Q(title__icontains=query) | Q(slug__icontains=query)
            )
        return object_list


class PostDetails(generic.DetailView):
    model = post
    template_name = 'post_detail.html'
