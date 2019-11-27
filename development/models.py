from django.db import models
# 引入富文本编辑器
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Development(models.Model):

    story_line_photo = models.ImageField(verbose_name='故事时间线图片', upload_to='story_line_photo', null=True, blank=True)  # 故事时间线图片

    story_title = RichTextUploadingField(verbose_name='故事标题', null=True, blank=True)  # 故事标题

    story_text = RichTextUploadingField(verbose_name='事件简要说明')  # 事件简要说明

    story_time = models.DateTimeField(verbose_name='故事发布')  # 事件发生事件

    story_time_update = models.DateTimeField(blank=True, null=True, verbose_name='更新时间')  # 故事更新时间

    class Meta:
        verbose_name = '网站更新内容'
        verbose_name_plural = '网站更新内容'