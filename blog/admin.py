from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title', )
    ordering = ['id', ]


admin.site.register(Article, ArticleAdmin)
