from django.contrib import admin

from .models import FeArticle, FeComment, FeModule, FeOption, FeTag

admin.site.register([FeArticle, FeComment, FeModule, FeOption, FeTag])
admin.site.site_header = 'Fedax后台管理'
admin.site.site_title = 'Fedax'
