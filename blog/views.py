from django.shortcuts import render
from .models import Article
from django.http import HttpResponse


def index(request):
    articles = Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})
