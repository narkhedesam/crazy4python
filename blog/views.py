from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.db.models import Q
from .models import post
from .forms import CommentForm

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
        object_list = []
        if query:
            object_list = post.objects.filter(
                Q(title__icontains=query) | Q(slug__icontains=query)
            )
        return object_list


def PostDetails(request, slug):
    template_name = 'post_detail.html'
    Post = get_object_or_404(post, slug=slug)
    Post.total_views += 1
    Post.save()
    comments = Post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = Post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': Post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})
