from django.contrib import admin

from webapp.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status', 'date']
    list_display_links = ['title']
    list_filter = ['author']
    search_fields = ['title', 'content']
    fields = ['title', 'author', 'content', 'date']
    readonly_fields = ['created_at', 'date']


admin.site.register(Article, ArticleAdmin)
