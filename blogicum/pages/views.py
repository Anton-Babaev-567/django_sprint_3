"""Pages/views.py."""
from django.shortcuts import render


def about(request):
    """About."""
    template_name = 'pages/about.html'
    return render(request, template_name)


def rules(request):
    """Rules."""
    template_name = 'pages/rules.html'
    return render(request, template_name)
