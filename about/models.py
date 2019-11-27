from django.db import models
# 引入富文本编辑器
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class SkillType(models.Model):
    name = models.CharField('技能分类',max_length=20,default='')

    class Meta:
        verbose_name = '技能类别'
        verbose_name_plural = '技能类别'
    
    def __str__(self):
        return self.name

class AboutWebSkill(models.Model):
    
    name = models.CharField(verbose_name='姓名', max_length=20, default='')
    introduce_text = models.TextField(verbose_name='个人简介')
    introduce_image = models.ImageField(verbose_name='个人头像', upload_to='myself_photo/%Y%m%d/', null=True, blank=True)
    skill = models.TextField(verbose_name='技能')
    # 技能类别采用一对多形式，一个技能属于一个类别，但一个类别中有多个技能
    skill_type = models.ForeignKey(SkillType, verbose_name='技能分类', default=None, on_delete=models.CASCADE)
    skill_open_time = models.DateTimeField(verbose_name='技能解锁时间')
    skill_status = models.TextField(verbose_name='目前状态')

    class Meta:
        verbose_name = '个人介绍'
        verbose_name_plural = '个人介绍'

    def __str__(self):
        return self.name

class About_models(models.Model):

    # 关于我小模块
    introduce = models.CharField(verbose_name='关于部门模块', max_length=20, default='')
    # 模块内容
    body = RichTextUploadingField(verbose_name='文章内容')
    # 创建时间
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 更新时间
    time_update = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '关于部分说明'
        verbose_name_plural = '关于部分'

    def __str__(self):
        return self.introduce