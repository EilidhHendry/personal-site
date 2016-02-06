from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blogengine.models import Post

def getRecentPosts(request):
    posts = Post.objects.all()
    sorted_posts = posts.order_by('-published_date')
    paginator = Paginator(sorted_posts, 2) 
    
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an int give page 1
        post_list = paginator.page(1)     
    except EmptyRange:
        # if page out of range give last page
        post_list = paginator.page(paginator.num_pages) 
    
    return render(request, 'blogengine/posts.html', {'posts':post_list})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blogengine/post_detail.html', {'post': post})
