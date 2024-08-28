"""Blog/views."""
from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.utils.timezone import now


def index(request):
    """Index."""
    template_name = 'blog/index.html'
    post_list = Post.objects.select_related(
        'author', 'category', 'location',
    ).filter(
        is_published=True,
        pub_date__lt=now(),
        category__is_published=True,
    )[:5]
    context = {
        'post_list': post_list
    }
    return render(request, template_name, context)


def post_detail(request, post_id):
    """Post."""
    template_name = 'blog/detail.html'
    post = get_object_or_404(
        Post.objects.select_related(
            'author', 'category', 'location',
        ).filter(
            is_published=True,
            pub_date__lt=now(),
            category__is_published=True,
        ),
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
        Category.objects.filter(
            is_published=True
        ),
        slug=category_slug)
    post_list = Post.objects.select_related(
        'author', 'category', 'location',
    ).filter(
        is_published=True,
        pub_date__lt=now(),
        category__slug=category_slug
    )
    context = {
        'post_list': post_list,
        'category': category,
    }

    return render(request, template_name, context)
