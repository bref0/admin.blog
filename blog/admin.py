from django.contrib import admin

from .models import Article, Comment, Module, Option, Tag, SinglePage


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag_name', 'update_time')
    list_display_links = ('tag_name',)
    list_per_page = 10
    search_fields = ('tag_name',)
    empty_value_display = ' -- '
    date_hierarchy = 'update_time'  # 详细时间分层筛选　
    ordering = ('-id',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'article_title', 'update_time')
    list_display_links = ('article_title',)
    list_per_page = 10
    search_fields = ('article_title',)
    empty_value_display = ' -- '
    list_filter = ('article_status',)  # 过滤器
    date_hierarchy = 'update_time'  # 详细时间分层筛选　
    ordering = ('-id',)
    filter_horizontal = ('tags',)

    def get_readonly_fields(self, request, obj=None):
        return self.readonly_fields

    readonly_fields = ('article_reading_volume', 'article_like_volume', 'article_comment_volume',)


@admin.register(Module)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'module_name', 'update_time')
    list_display_links = ('module_name',)
    list_per_page = 10
    search_fields = ('module_name',)
    empty_value_display = ' -- '
    date_hierarchy = 'update_time'
    ordering = ('-id',)

    def has_add_permission(self, request):  # 禁止添加
        return False

    def has_delete_permission(self, request, obj=None):  # 禁止删除
        return False


@admin.register(SinglePage)
class SinglePageAdmin(admin.ModelAdmin):
    list_display = ('id', 'page_name', 'page_route', 'update_time')
    list_display_links = ('page_name',)
    list_per_page = 10
    search_fields = ('page_name', 'page_route')
    empty_value_display = ' -- '
    date_hierarchy = 'update_time'  # 详细时间分层筛选　
    ordering = ('-id',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment_article_id', 'create_time')
    date_hierarchy = 'create_time'  # 详细时间分层筛选　
    ordering = ('-id',)


admin.site.register([Option])

admin.site.site_header = 'Fedax后台管理'
admin.site.site_title = 'Fedax'
