from django.contrib import admin

from pythonsucks.article.models import Article


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    prepopulated_fields = {"slug": ["title"]}


admin.site.register(Article, ArticleAdmin)
