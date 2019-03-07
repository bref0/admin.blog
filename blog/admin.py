from django.contrib import admin

from .models import Article, Comment, Module, Option, Tag


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'article_title', 'update_time')
    list_per_page = 10
    search_fields = ('article_title',)
    empty_value_display = ' -- '
    ordering = ('-id',)

    def get_readonly_fields(self, request, obj=None):
        return self.readonly_fields

    readonly_fields = ('create_time',)


admin.site.register([Comment, Module, Option, Tag])

admin.site.site_header = 'Fedax后台管理'
admin.site.site_title = 'Fedax'
