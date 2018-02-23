from django.shortcuts import render
from .models import BlogArticles


def blog_title(request):
    articles = BlogArticles.objects.all()
    return render(request, 'blog/titles.html', {'blog': articles})
