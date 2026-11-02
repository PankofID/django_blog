from django.shortcuts import render, get_object_or_404

from main.models import Post


# Create your views here.

def index(request):
    popular_posts = Post.objects.order_by('-views')[:3]
    recent_posts = Post.objects.order_by('-created_at')[:5]

    context = {
        'popular_posts': popular_posts,
        'recent_posts': recent_posts,
    }

    return render(request, 'main/index.html', context)

def about(request):
    return render(request, 'main/about.html')

def posts(request):
    posts_list = Post.objects.order_by('-created_at')

    context = {
        'posts_list': posts_list
    }

    return render(request, 'main/posts.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    context = {
        'post': post,
    }

    return render(request, 'main/post_detail.html', context)

def contact(request):
    return render(request, 'main/contact.html')