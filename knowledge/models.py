from django.db import models
from django.utils import timezone
# Create your models here.
class MyKnowledgeUrl(models.Model):
    # 资料名称
    name = models.CharField(max_length=100, blank=True, verbose_name='资料名称')
    # 创建时间
    create_time = models.DateTimeField(default=timezone.now, verbose_name='时间')
    # 网站链接
    search_url = models.URLField(max_length=100, blank=True, verbose_name='资料链接')

    class Meta:
        verbose_name = '网站分享'
        verbose_name_plural = '网站资料列表'

    def __str__(self):
        return self.name


class MyBookShare(models.Model):
    # 资料名称
    title = models.CharField(max_length=100, blank=True, verbose_name='图书名称')
    # 创建时间
    create_time = models.DateTimeField(default=timezone.now, verbose_name='时间')
    # 网站链接
    download = models.URLField(max_length=100, blank=True, verbose_name='下载地址')

    class Meta:
        verbose_name = '图书分享'
        verbose_name_plural = '图书分享列表'

    def __str__(self):
        return self.title

class MySoftware(models.Model):
    # 软件名称
    title = models.CharField(max_length=100, blank=True, verbose_name='软件名称')
    # 创建时间
    create_time = models.DateTimeField(default=timezone.now, verbose_name='时间')
    # 下载链接
    download = models.URLField(max_length=100, blank=True, verbose_name='下载地址')

    class Meta:
        verbose_name = '软件分享'
        verbose_name_plural = '软件分享列表'

    def __str__(self):
        return self.title