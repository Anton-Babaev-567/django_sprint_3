"""Blog/views."""
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now

from .models import Post, Category

POSTS_PER_PAGE = 5


def get_filtered_qs(queryset, **kwargs):

    filters = {
        'is_published': True,
        'pub_date__lt': now(),
        'category__is_published': True,
    }
    filters.update(kwargs)
    return queryset.select_related(
        'author', 'category', 'location').filter(**filters)


def index(request):
    """Index."""
    template_name = 'blog/index.html'
    posts = get_filtered_qs(Post.objects.all())[:POSTS_PER_PAGE]
    context = {
        'post_list': posts
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
    post_list = get_filtered_qs(
        Post.objects.all(),
        category__slug=category_slug
    )
    context = {
        'post_list': post_list,
        'category': category,
    }
    return render(request, template_name, context)
