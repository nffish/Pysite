from django.shortcuts import render
from django.http import HttpResponse

from . import models
from .models import Article


def index(request):
    articles = Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})


def article_view(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article': article})
