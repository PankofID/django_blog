from django.db.models import Q, F, Count
from django.shortcuts import render, get_object_or_404

from main.models import Post, Category


# Create your views here.

def index(request):
    popular_posts = Post.objects.order_by('-views')[:3]
    recent_posts = Post.objects.order_by('-created_at')[:5]
    categories = Category.objects.annotate(post_count=Count('posts'))

    context = {
        'popular_posts': popular_posts,
        'recent_posts': recent_posts,
        'categories': categories,
    }

    return render(request, 'main/index.html', context)

def about(request):
    return render(request, 'main/about.html')

def posts(request):
    category_slug = request.GET.get('category')
    search_query = request.GET.get('q', '').strip()

    posts_list = Post.objects.select_related('category').order_by('-created_at')
    if category_slug:
        posts_list = posts_list.filter(category__slug=category_slug)
    if search_query:
        posts_list = posts_list.filter(
            Q(title__icontains=search_query)
            | Q(content__icontains=search_query)
            | Q(category__name__icontains=search_query)
        )

    categories = Category.objects.all()

    context = {
        'posts_list': posts_list,
        'categories': categories,
        'active_category': category_slug,
        'search_query': search_query,
    }

    return render(request, 'main/posts.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    viewed_post = request.session.get('viewed_post', [])
    if post.id not in viewed_post:
        Post.objects.filter(id=post.id).update(views=F('views') + 1)

    viewed_post.append(post.id)
    request.session['viewed_post'] = viewed_post

    context = {
        'post': post,
    }

    return render(request, 'main/post_detail.html', context)

def contact(request):
    return render(request, 'main/contact.html')