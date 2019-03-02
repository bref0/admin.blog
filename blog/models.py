# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class FeArticle(models.Model):
    article_title = models.CharField(max_length=50, verbose_name='标题')
    article_tag_ids = models.CharField(max_length=50)
    article_summary = models.CharField(max_length=255)
    article_content = models.TextField()
    article_status = models.IntegerField()
    article_reading_volume = models.IntegerField()
    article_like_volume = models.IntegerField()
    article_comment_volume = models.IntegerField()
    article_sticky_posts = models.IntegerField()
    create_time = models.PositiveIntegerField(blank=True, null=True, verbose_name='创建时间', editable=False)
    update_time = models.PositiveIntegerField(blank=True, null=True, verbose_name='更新时间')
    delete_time = models.IntegerField(blank=True, null=True, verbose_name='删除时间')

    # pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    # update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    def __str__(self):
        return self.article_title

    class Meta:
        verbose_name = '文章列表'
        verbose_name_plural = '文章列表'
        app_label = 'blog'
        db_table = 'fe_article'


class FeComment(models.Model):
    id = models.BigAutoField(primary_key=True)
    comment_article_id = models.BigIntegerField()
    comment_author_email = models.CharField(max_length=100)
    comment_author_ip = models.CharField(max_length=100)
    comment_content = models.TextField()
    comment_approved = models.IntegerField()
    comment_parent = models.PositiveIntegerField()
    update_time = models.IntegerField()
    create_time = models.IntegerField()
    delete_time = models.IntegerField(blank=True, null=True)

    class Meta:
        app_label = 'blog'
        db_table = 'fe_comment'


class FeModule(models.Model):
    module_name = models.CharField(max_length=30)
    module_route = models.CharField(max_length=30)
    module_status = models.IntegerField()
    create_time = models.IntegerField(blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)
    delete_time = models.IntegerField(blank=True, null=True)

    class Meta:
        app_label = 'blog'

        db_table = 'fe_module'


class FeOption(models.Model):
    option_name = models.CharField(unique=True, max_length=64)
    option_value = models.TextField(blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)
    delete_time = models.IntegerField(blank=True, null=True)

    class Meta:
        app_label = 'blog'

        db_table = 'fe_option'


class FeTag(models.Model):
    tag_name = models.CharField(max_length=30)
    tag_desc = models.CharField(max_length=255)
    delete_time = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)

    class Meta:
        app_label = 'blog'

        db_table = 'fe_tag'
