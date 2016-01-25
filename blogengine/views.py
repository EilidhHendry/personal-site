from django.shortcuts import render_to_response, render, get_object_or_404
from blogengine.models import Post

def getRecentPosts(request):
    posts = Post.objects.all()

    sorted_posts = posts.order_by('-published_date')

    return render_to_response('posts.html', {'posts':sorted_posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})
