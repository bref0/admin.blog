from django.contrib import admin

from .models import Article, Comment, Module, Option, Tag

admin.site.register([Article, Comment, Module, Option, Tag])
admin.site.site_header = 'Fedax后台管理'
admin.site.site_title = 'Fedax'
