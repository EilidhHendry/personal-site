from django.shortcuts import render_to_response
from blogengine.models import Post

def getRecentPosts(request):
    posts = Post.objects.all()

    sorted_posts = posts.order_by('-pub_date')

    return render_to_response('posts.html', {'posts':sorted_posts})
