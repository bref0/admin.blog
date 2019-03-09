# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from ckeditor.fields import RichTextField
import datetime


class Article(models.Model):
    Article_Status_CHOICES = (
        (1, '显示'),
        (2, '隐藏'),
    )
    article_title = models.CharField(max_length=50, verbose_name='标题')
    article_tag_ids = models.CharField(max_length=50, verbose_name='标签')
    article_summary = models.CharField(max_length=255, verbose_name='摘要')
    article_content = RichTextField(verbose_name='内容')
    article_status = models.IntegerField(verbose_name='状态',
                                         null=False,
                                         choices=Article_Status_CHOICES,
                                         default='1')
    article_reading_volume = models.IntegerField(verbose_name='浏览量')
    article_like_volume = models.IntegerField(verbose_name='点赞数')
    article_comment_volume = models.IntegerField(verbose_name='评论数')
    article_sticky_posts = models.IntegerField(verbose_name='是否置顶')
    create_time = models.PositiveIntegerField(blank=True,
                                              null=True,
                                              verbose_name='创建时间',
                                              )
    update_time = models.PositiveIntegerField(blank=True,
                                              null=True,
                                              verbose_name='更新时间',
                                              editable=False,
                                              default=datetime.datetime.now)
    delete_time = models.IntegerField(blank=True,
                                      null=True,
                                      editable=False,
                                      verbose_name='删除时间')

    def __str__(self):
        return self.article_title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
        app_label = 'blog'
        db_table = 'fe_article'


class Comment(models.Model):
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

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'
        app_label = 'blog'
        db_table = 'fe_comment'


class Module(models.Model):
    module_name = models.CharField(max_length=30)
    module_route = models.CharField(max_length=30)
    module_status = models.IntegerField()
    create_time = models.IntegerField(blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)
    delete_time = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.module_name

    class Meta:
        verbose_name = '模块'
        verbose_name_plural = '模块'
        app_label = 'blog'
        db_table = 'fe_module'


class Option(models.Model):
    option_name = models.CharField(unique=True, max_length=64)
    option_value = models.TextField(blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)
    delete_time = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.option_name

    class Meta:
        verbose_name = '配置'
        verbose_name_plural = '配置'
        app_label = 'blog'
        db_table = 'fe_option'


class Tag(models.Model):
    tag_name = models.CharField(max_length=30)
    tag_desc = models.CharField(max_length=255)
    delete_time = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'
        app_label = 'blog'
        db_table = 'fe_tag'
