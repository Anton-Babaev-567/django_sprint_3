"""Blog/views."""
from django.shortcuts import render, get_object_or_404

from .models import Post, Category
from .utils import get_filtered_qs

POSTS_PER_PAGE = 5


def index(request):
    """Index."""
    template_name = 'blog/index.html'
    posts = get_filtered_qs(Post.objects.all())[:POSTS_PER_PAGE]
    context = {
        'posts': posts
    }
    return render(request, template_name, context)


def post_detail(request, post_id):
    """Post."""
    template_name = 'blog/detail.html'
    post = get_object_or_404(
        get_filtered_qs(Post.objects.all()),
        id=post_id,
    )
    context = {
        'post': post
    }
    return render(request, template_name, context)


def category_posts(request, category_slug):
    """Category."""
    template_name = 'blog/category.html'
    category = get_object_or_404(
        Category.objects.filter(is_published=True),
        slug=category_slug
    )
    posts = get_filtered_qs(
        Post.objects.all(),
        category__slug=category_slug
    )
    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, template_name, context)
