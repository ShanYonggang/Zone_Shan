from django.db import models
from django.utils import timezone
from django.conf import settings
# 记得导入
from django.urls import reverse
# Django-taggit
from taggit.managers import TaggableManager
# 引入富文本编辑器
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class ArticleColumn(models.Model):
    # 文章分类名称
    title = models.CharField(max_length=100,blank=True)
    # 创建时间
    create_time = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-create_time',)
        verbose_name = '博客文章分类'
        verbose_name_plural = '博客文章分类'
    
    def __str__(self):
        return self.title

# Create your models here.
class ArticlePost(models.Model):
    # 文章作者
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, verbose_name='文章作者')
    # 文章标题
    title = models.CharField(max_length=100, verbose_name='文章标题')
    # 博客图片
    blog_photo = models.ImageField(upload_to='article/%Y%m%d/', verbose_name='博客文章图片',blank=True)
    # 文章正文
    body = RichTextUploadingField(verbose_name='文章内容')
    # 文章创建时间
    create_time = models.DateTimeField(default=timezone.now, verbose_name='文章创建时间')
    # 文章更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='文章更新时间')
    # 文章浏览量
    article_view = models.PositiveIntegerField(default=0)
    # 文章标签
    tags = TaggableManager(blank=True)
    # 文章分类（一篇文章对应一个分类，一个分类里可有多篇文章，因此采用一对多的关系关系）
    column = models.ForeignKey(ArticleColumn, null=True,blank=True,on_delete=models.CASCADE,verbose_name='文章分类')
    # 文章点赞数
    like = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('-create_time',)
        verbose_name = '博客文章'
        verbose_name_plural = '博客文章列表'

    def __str__(self):
        return self.title

    # 获取文章地址
    def get_absolute_url(self):
        return reverse('index:article_detail', args=[self.id])

class ArticleLikes(models.Model):
    # 点赞文章
    article = models.ForeignKey(ArticlePost,on_delete=models.DO_NOTHING,verbose_name='点赞文章')
    # 点赞用户
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING,verbose_name='点赞用户',blank=True,null=True,)
    # 点赞ip
    ip_address = models.GenericIPAddressField(verbose_name='点赞IP地址')
    # IP归属地
    ip_loaction = models.CharField(max_length=20,verbose_name='ip归属地',blank=True,null=True)
    # 创建时间
    time_create = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    # 更新时间
    time_update = models.DateTimeField(auto_now=True,blank=True,null=True,verbose_name='更新时间')

    class Meta:
        verbose_name = '文章点赞'
        verbose_name_plural = '文章点赞列表'

    def __str__(self):
        return '%s,%s'%(self.article,self.ip_address)

#
class ArticleDetailView(models.Model):
    # 访问文章
    article = models.ForeignKey(ArticlePost, on_delete=models.DO_NOTHING, verbose_name='其访问文章')
    # 访问文章ip
    ip_address = models.GenericIPAddressField(verbose_name='文章访问IP地址')
    # 访问数量
    visit_number = models.PositiveIntegerField(default=1, verbose_name='IP地址访问数量')
    # IP归属地
    ip_loaction = models.CharField(max_length=20,verbose_name='ip归属地',blank=True,null=True)
    # 创建时间
    time_create = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    # 更新时间
    time_update = models.DateTimeField(auto_now=True,blank=True,null=True,verbose_name='更新时间')

    class Meta:
        verbose_name = '文章访问IP统计'
        verbose_name_plural = '文章访问IP统计'

    def __str__(self):
        return '%s,%s'%(self.article, self.ip_address)


# IP访问量统计
class SeeMyWebsite(models.Model):
    # 访问IP地址
    ip_address = models.GenericIPAddressField(verbose_name='访问的IP地址')
    # 访问数量
    visit_number = models.PositiveIntegerField(default=1,verbose_name='IP地址访问数量')
    # IP归属地
    ip_loaction = models.CharField(max_length=20,verbose_name='ip归属地',blank=True,null=True)
    # 创建时间
    time_create = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    # 更新时间
    time_update = models.DateTimeField(auto_now=True,blank=True,null=True,verbose_name='更新时间')

    class Meta:
        verbose_name = '网站访问量'
        verbose_name_plural = '网站访问量'

    def __str__(self):
        return '%s,%s'%(self.visit_number,self.ip_address)
